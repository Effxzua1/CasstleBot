# casstle_web.py — sirve la web y /api/stats del bot (deja esta carpeta junto al bot: index.html + assets/)
import os, time
from aiohttp import web

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(ROOT, "index.html")
ASSETS = os.path.join(ROOT, "assets")


def start_web(bot, port=8080, **_ignorados):
    async def index(request):
        return web.FileResponse(PAGE)

    async def stats(request):
        users = sum((g.member_count or 0) for g in bot.guilds)
        cmds = len({c.qualified_name for c in bot.walk_commands()})
        lat = bot.latency
        return web.json_response({
            "servers": len(bot.guilds),
            "users": users,
            "commands": cmds,
            "ping": round(lat * 1000) if lat == lat else 0,
            "uptime": int(time.time() - getattr(bot, "start_time", time.time())),
        }, headers={"Access-Control-Allow-Origin": "*", "Cache-Control": "no-store"})

    started = {"ok": False}

    @bot.listen("on_ready")
    async def _casstle_web_ready():
        if started["ok"]:
            return
        started["ok"] = True
        app = web.Application()
        app.router.add_get("/", index)
        app.router.add_get("/api/stats", stats)
        app.router.add_static("/assets", ASSETS)
        runner = web.AppRunner(app)
        await runner.setup()
        await web.TCPSite(runner, "0.0.0.0", port).start()
        print(f"Casstle · web lista en http://localhost:{port}")
