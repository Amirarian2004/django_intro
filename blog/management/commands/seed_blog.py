from django.core.management.base import BaseCommand

from blog.models import Category, Post, Tag


class Command(BaseCommand):
    help = 'Seed categories and posts for practice'

    def handle(self, *args, **options):
        names = ['Tech', 'Life', 'Fitness', 'Gaming', 'Study']
        cats = [Category.objects.get_or_create(name=n)[0] for n in names]

        tag_names = ['django', 'orm', 'sql', 'git',
                     'python', 'postgres', 'api', 'unused']
        tags = [Tag.objects.get_or_create(name=n)[0] for n in tag_names]
        used = tags[:-1]

        for i in range(30):
            post, _ = Post.objects.get_or_create(
                title=f'Seed post {i + 1}',
                defaults={
                    'content': f'Content for seed post {i + 1}',
                    'category': cats[i % len(cats)],
                },
            )
            post.tags.add(
                used[i % len(used)],
                used[(i + 2) % len(used)],
            )
            if i % 3 == 0:
                post.tags.add(used[(i + 4) % len(used)])

        self.stdout.write(self.style.SUCCESS('Seeded.'))