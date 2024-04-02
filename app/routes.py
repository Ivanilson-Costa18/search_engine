
from flask import request, render_template, redirect
from app import app
from app.utils import prepare_results
import time

@app.route('/')
def landing():
    return render_template('home.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    
    if query == "":
        return redirect('/')
    
    app.logger.debug(f'Sending "{query}" to find matches')

    start_time = time.time()
    results = prepare_results(query)
    results_seconds = time.time() - start_time
    results["time"] = format(results_seconds, ".2f")

    return render_template('search.html', query=query, results=results)