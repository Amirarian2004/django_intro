from django.core.management.base import BaseCommand

from blog.models import Category, Post


class Command(BaseCommand):
    help = 'Seed categories and posts for practice'

    def handle(self, *args, **options):
        names = ['Tech', 'Life', 'Fitness', 'Gaming', 'Study']
        cats = [Category.objects.get_or_create(name=n)[0] for n in names]

        for i in range(30):
            Post.objects.get_or_create(
                title=f'Seed post {i + 1}',
                defaults={
                    'content': f'Content for seed post {i + 1}',
                    'category': cats[i % len(cats)],
                },
            )

        self.stdout.write(self.style.SUCCESS('Seeded.'))