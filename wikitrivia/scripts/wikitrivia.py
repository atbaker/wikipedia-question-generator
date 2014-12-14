from wikitrivia.article import Article

import click
import json

@click.command()
@click.argument('title')
@click.option('--output', default=False, help='Output to JSON file')
def generate_trivia(title, output):
    """Generates trivia questions from wikipedia articles"""
    article = Article(title=title)
    questions = article.generate_trivia_sentences()

    if output:
      with open(output, 'w') as json_file:
        json.dump(questions, json_file)
        click.echo('Output stored in {0}'.format(output))
    else:
      click.echo(questions)

if __name__ == '__main__':
    generate_trivia()
