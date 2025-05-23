from django.test import TestCase, Client
from django.urls import reverse
from main.models import CV
import random

class CVListViewTests(TestCase):
    fixtures = ['skills.json', 'projects.json', 'cv.json']

    def setUp(self):
        self.client = Client()

    def test_list_view_status_code(self):
        response = self.client.get(reverse('main:cv_list'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_uses_correct_template(self):
        response = self.client.get(reverse('main:cv_list'))
        self.assertTemplateUsed(response, 'main/cv_list.html')

    def test_list_view_context(self):
        response = self.client.get(reverse('main:cv_list'))
        cvs = response.context['cvs']
        total = len(cvs)
        print(f"\nTesting CV list view: found {total} entries")
        for idx, cv in enumerate(cvs, start=1):
            skill_names    = [skill.name for skill in cv.skills.all()]
            project_titles = [proj.title for proj in cv.projects.all()]
            email          = cv.contacts.get('email')
            phone          = cv.contacts.get('phone')
            print(
                f"  Entry {idx}/{total}: "
                f"PK={cv.pk} | Name={cv.firstname} {cv.lastname} | "
                f"Skills={skill_names} | Projects={project_titles} | "
                f"Email={email or 'N/A'} | Phone={phone or 'N/A'}"
            )
            # Assertions for rendered content
            self.assertContains(response, cv.firstname)
            self.assertContains(response, cv.lastname)
            for name in skill_names:
                self.assertContains(response, name)
            # we not rendering next things
            #for title in project_titles:
            #    self.assertContains(response, title)
            #if email:
            #    self.assertContains(response, email)
            #if phone:
            #    self.assertContains(response, phone)

        # Ensure at least one CV was listed
        self.assertTrue(total >= 1)


class CVDetailViewTests(TestCase):
    fixtures = ['skills.json', 'projects.json', 'cv.json']

    def setUp(self):
        self.client = Client()
        all_cvs = list(CV.objects.all())
        self.cvs = random.sample(all_cvs, min(5, len(all_cvs)))

    def test_detail_views_for_multiple_cvs(self):
        total = len(self.cvs)
        for idx, cv in enumerate(self.cvs, start=1):
            skill_names    = [skill.name for skill in cv.skills.all()]
            project_titles = [proj.title for proj in cv.projects.all()]
            email          = cv.contacts.get('email')
            phone          = cv.contacts.get('phone')
            print(
                f"\nTesting CV detail {idx}/{total}: "
                f"PK={cv.pk} | Name={cv.firstname} {cv.lastname} | "
                f"Skills={skill_names} | Projects={project_titles} | "
                f"Email={email or 'N/A'} | Phone={phone or 'N/A'}"
            )
            url = reverse('main:cv_detail', args=[cv.pk])
            response = self.client.get(url)

            # Status code & template
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'main/cv_detail.html')

            # Context and content checks
            self.assertEqual(response.context['cv'], cv)
            self.assertContains(response, cv.firstname)
            self.assertContains(response, cv.lastname)
            self.assertContains(response, cv.bio)
            for name in skill_names:
                self.assertContains(response, name)
            for title in project_titles:
                self.assertContains(response, title)
            if email:
                self.assertContains(response, email)
            if phone:
                self.assertContains(response, phone)
				
