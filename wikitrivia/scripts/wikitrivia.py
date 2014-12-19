from wikitrivia.article import Article

import click
import json

# For now, hard-code the titles of articles you want to scrape here
ARTICLES = (
    'Tony Bennett',
    'Python (programming language)',
    'Henry V, Duke of Carinthia',
    'Scabbling',
    'Globe of the Great Southwest',
    'Ukrainian Women\'s Volleyball Super League'
)

@click.command()
@click.option('--output', default=False, help='Output to JSON file')
def generate_trivia(output):
    """Generates trivia questions from wikipedia articles"""
    questions = []
    for article in ARTICLES:
        article = Article(title=article)
        questions = questions + article.generate_trivia_sentences()

    if output:
      with open(output, 'w') as json_file:
        json.dump(questions, json_file)
        click.echo('Output stored in {0}'.format(output))
    else:
      click.echo(questions)

if __name__ == '__main__':
    generate_trivia()
