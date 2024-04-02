
import time
from app import app
from app.utils import prepare_results, get_suggestions_from_titles
from flask import request, render_template, redirect

@app.route('/')
def landing():
    """
    Render the landing page.

    Returns:
        str: The rendered HTML content of the landing page.
    """
    return render_template('home.html')

@app.route("/suggestions")
def get_suggestions():
    """
    Return title suggestions based on the query parameter.

    Query parameter:
        q (str): Query string used for filtering titles.

    Returns:
        dict: A dictionary containing a list of title suggestions.
    """
    query = request.args.get('q')

    app.logger.debug(f'Finding suggestion for "{query}".')

    results = get_suggestions_from_titles(query.lower())

    return results

@app.route('/search')
def search():
    """
    Perform a search based on the provided query.

    This route function handles search queries.
    It retrieves the query string from the request parameters, checks if it's empty,
    logs the query for debugging purposes, measures the time taken to retrieve and
    format search results, and renders the 'search.html' template with the query and
    formatted search results.

    Query parameter:
        q (str): Query string used for searching.

    Returns:
        str: The rendered HTML content of the search results page.
    """
    query = request.args.get('q')

    if query == "":
        return redirect('/')

    app.logger.debug(f'Sending "{query}" to find matches')

    start_time = time.time()
    results = prepare_results(query)
    results_seconds = time.time() - start_time
    results["time"] = format(results_seconds, ".2f")

    return render_template('search.html', query=query, results=results)
