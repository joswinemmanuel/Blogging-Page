from django.test import TestCase
from django.urls import reverse

from blog.models import Post


class PostListViewTests(TestCase):
    def test_posts_visible(self):
        post = Post.objects.create(
            title="A title", body="Blog content.", slug="test-slug"
        )

        url = reverse("posts")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        # Special Django Helper Method
        self.assertQuerysetEqual(response.context["post_list"], ["<Post: A title>"])

        # Test the webpage content contains our post body.
        self.assertContains(response, "Blog content.")
