max_chapters = -1
book_with_max = ''

with open('books_and_chapters.txt') as book_file:
    for line in book_file:
        parts = line.split(':')
        book = parts[0].strip()
        chapters = int(parts[1])
        scripture = parts[2].strip()
        print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapters}')

        if chapters > max_chapters:
            max_chapters = chapters
            book_with_max = book

print()
print(f'The book with the most chapters is: {book_with_max}.')
print(f'It has {max_chapters} chapters.')