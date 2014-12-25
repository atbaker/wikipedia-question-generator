from wikitrivia.article import Article

import click
import json

# For now, hard-code the titles of articles you want to scrape here
SAMPLE_ARTICLES = (
    'Tony Bennett',
    'Gauls',
    'Henry V, Duke of Carinthia',
    'Scabbling',
    'Ukrainian Women\'s Volleyball Super League'
)

@click.command()
@click.argument('titles', nargs=-1)
@click.option('--output', default=False, help='Output to JSON file')
def generate_trivia(titles, output):
    """Generates trivia questions from wikipedia articles. If no
    titles are supplied, pulls from these sample articles:

    'Tony Bennett', 'Python (programming language)', 'Scabbling',
    'Ukrainian Women\'s Volleyball Super League'
    """
    # Use the sample articles if the user didn't supply any
    if len(titles) == 0:
        titles = SAMPLE_ARTICLES

    # Retrieve the trivia sentences
    questions = []
    for article in titles:
        article = Article(title=article)
        questions = questions + article.generate_trivia_sentences()

    # Output to stdout or JSON
    if output:
      with open(output, 'w') as json_file:
        json.dump(questions, json_file)
        click.echo('Output stored in {0}'.format(output))
    else:
      click.echo(questions)

if __name__ == '__main__':
    generate_trivia()
