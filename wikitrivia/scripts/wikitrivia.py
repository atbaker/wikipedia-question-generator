import click

from wikitrivia.article import Article

@click.command()
@click.argument('title')
@click.option('--json', default=False, help='Output to JSON file')
def generate_trivia(title, json):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('Goodbye %s!' % title)
    article = Article(title=title)
    click.echo(article.summary)

    click.echo(article.generate_trivia_sentences())

if __name__ == '__main__':
    generate_trivia()
