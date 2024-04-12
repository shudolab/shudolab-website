from datetime import datetime
import glob
import frontmatter



# invalid_datetime_str = 'Wed, 24 Jan 2018 08:42:56 +0000'
invalid_datetime_format = '%a, %d %b %Y %H:%M:%S +0000'
# output_format = '2024-02-02T04:14:54-08:00'
output_format = '%Y-%m-%dT%H:%M:%S+09:00'
# 2024-04-13T01:03:46+09:00


def process_file(infile):
    with open(infile) as fd:
        print(fd.read())

    post = frontmatter.load(infile)
    # print(post)
    if 'date' in post:
        try:
            print(post['date'])
            parsed = datetime.strptime(post['date'], invalid_datetime_format)
        except ValueError as e:
            # 間違ったフォーマットじゃないときはエラーでる
            print('Error:', e)
        except TypeError as e:
            # YAMLのdatetimeフォーマットに従っているとパースエラー
            print('Error:', e)
        else:
            print(post['date'])
            # print(parsed)
            print(parsed.strftime(output_format))
            post['date'] = parsed.strftime(output_format)

    if 'tags' in post:
        del post['tags']
    return frontmatter.dumps(post)


def main():
    # ret = process_file('content/posts/国際会議-ieee-icce-2023-にて-best-student-paper-award-を受賞-2023年-1月.md')
    # print(ret)

    for path in glob.glob('content/**/*.md'):
        print(path)
        ret = process_file(path)
        # print(ret)
        with open(path, 'w') as fd:
            fd.write(ret)


if __name__ == '__main__':
    main()


