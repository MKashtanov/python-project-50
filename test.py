from gendiff.gendiff import generate_diff

if __name__ == '__main__':
    print(generate_diff(
        './tests/fixtures/file3.json', './tests/fixtures/file4.json',
        format_name='stylish')
    )
