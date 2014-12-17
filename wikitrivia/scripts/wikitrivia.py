from wikitrivia.article import Article

import click
import json

# Tony Bennett
# The Room
# Denmark
# Benedict Arnold
# Communism
# Ukranian Women's Volleyball Super-league

ARTICLES = (
    'Tony Bennett',
    'The Room (film)',
    'Denmark',
    'Benedict Arnold',
    'Communism',
    'Ukrainian Women\'s Volleyball Super League'
)

@click.command()
@click.argument('title')
@click.option('--output', default=False, help='Output to JSON file')
def generate_trivia(title, output):
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
