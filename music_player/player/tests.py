from django.test import TestCase
from django.urls import reverse
from .models import Song

class SongViewTests(TestCase):

    def setUp(self):
        # Create test songs
        self.song1 = Song.objects.create(title='Song One', author='Author A', img='media/song1_cover.jpg', audio='media/song1.mp3')
        self.song2 = Song.objects.create(title='Song Two', author='Author A', img='media/song2_cover.jpg', audio='media/song2.mp3')
        self.song3 = Song.objects.create(title='Song Three', author='Author B', img=None, audio='media/song3.mp3')  # Missing image

    def test_index_view_status_code(self):
        response = self.client.get(reverse('index'))  # Update with your URL name
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))  # Update with your URL name
        self.assertTemplateUsed(response, 'player/index.html')

    def test_index_view_retrieves_songs_in_order(self):
        response = self.client.get(reverse('index'))  # Update with your URL name
        songs = response.context['songs']
        self.assertEqual(list(songs), [self.song2, self.song1, self.song3])  # Verify order: Author A's songs first, then Author B's

    def test_index_view_context_song_objs_list(self):
        response = self.client.get(reverse('index'))  # Update with your URL name
        song_objs_list = response.context['song_objs_list']

        # Check that song_objs_list contains expected data
        self.assertEqual(len(song_objs_list), 3)

        self.assertEqual(song_objs_list[0]['title'], 'Song Two')  # First in order
        self.assertEqual(song_objs_list[1]['title'], 'Song One')  # Second in order
        self.assertEqual(song_objs_list[2]['title'], 'Song Three')  # Last in order

        # Verify the missing image defaults to "media/default_cover.jpg"
        self.assertEqual(song_objs_list[2]['img'], 'media/default_cover.jpg')

    def test_index_view_context_numbered_songs(self):
        response = self.client.get(reverse('index'))  # Update with your URL name
        numbered_songs = response.context['numbered_songs']
        increased_nums = [num + 1 for num in range(len(numbered_songs))]

        # Verify the numbering is correct
        for index, (song, num, inc_num) in enumerate(numbered_songs):
            self.assertEqual(num, index)
            self.assertEqual(inc_num, index + 1)
