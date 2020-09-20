web: pytest shortener_app/test_main.py --html-report=./static/report.html
web: uvicorn shortener_app.main:app --limit-concurrency 100 --workers 4  --host=0.0.0.0 --port=${PORT:-5000}
