import functools
import http.server
import socketserver

ROOT = r'C:\Users\Wiryl\Sol Dev\Ensemble-Website-Worktrees\site-v2-2-mascot-placement-study-2026-09-16'
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
with socketserver.TCPServer(('127.0.0.1', 8877), handler) as server:
    print(f'Serving {ROOT} on 8877', flush=True)
    server.serve_forever()

