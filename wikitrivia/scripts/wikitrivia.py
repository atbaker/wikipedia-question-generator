import click

from wikitrivia.article import Article

@click.command()
@click.argument('title')
@click.option('--json', default=False, help='Output to JSON file')
def generate_trivia(title, json):
    """Generates trivia questions from wikipedia articles"""
    article = Article(title=title)
    click.echo(article.generate_trivia_sentences())

if __name__ == '__main__':
    generate_trivia()
