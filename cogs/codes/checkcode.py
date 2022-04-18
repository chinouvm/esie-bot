from datetime import datetime, timezone
import discord
from discord.ext import commands, tasks
from database import db


class BackgroundTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=5)  # <- will do this every 5 seconds
    async def check(guild):
        for member in guild.members:
            if member is not None:
                results = db.collection(u'users').document(member.name).get()
                if results.exists == False:
                    ref = db.collection(u'users').document(member.name)
                    ref.set({
                        u'started': "",
                        u'playedvscode': False,
                        u'totalminutes': 0
                    })
                results = db.collection(u'users').document(member.name).get()
                if results.exists:
                    playedvscode = results.to_dict()['playedvscode']
                if member.activity is not None:
                    if len(member.activities) > 1 and playedvscode == False:
                        if member.activities[1].name == "Visual Studio Code":
                            started = datetime.now(timezone.utc)
                            db.collection(u'users').document(
                                member.name).update({"playedvscode": True})
                            db.collection(u'users').document(
                                member.name).update({"started": started.strftime(
                                    "%Y-%m-%d %H:%M:%S.%f+00:00")})
                    else:
                        if member.activities[0].name == "Visual Studio Code" and playedvscode == False:
                            started = datetime.now(timezone.utc)
                            db.collection(u'users').document(member.name).update(
                                {"playedvscode": True})
                            db.collection(u'users').document(member.name).update(
                                {"started": started.strftime(
                                    "%Y-%m-%d %H:%M:%S.%f+00:00")})
                    if playedvscode == True:
                        end = datetime.now(timezone.utc).strftime(
                            "%Y-%m-%d %H:%M:%S.%f+00:00")

                        results = db.collection(
                            u'users').document(member.name).get()
                        if results.exists:
                            started = results.to_dict()['started']
                        if started != "":
                            date_format_str = "%Y-%m-%d %H:%M:%S.%f+00:00"
                            fmtstarted = datetime.strptime(
                                started, date_format_str)
                            fmtend = datetime.strptime(
                                end, date_format_str)
                            diff = fmtend - fmtstarted
                            diff_in_minutes = diff.total_seconds() / 60

                            results = db.collection(
                                u'users').document(member.name).get()
                            if results.exists:
                                min = results.to_dict()['totalminutes']
                            db.collection(u'users').document(member.name).update(
                                {"totalminutes": min + diff_in_minutes})
                            db.collection(u'users').document(member.name).update(
                                {"playedvscode": False})
