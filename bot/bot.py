import disnake, random, time
from disnake.ext import commands, tasks
from disnake import Intents
from disnake.ext.commands.core import has_permissions
from os import environ
# import pygsheets

class shiinaBot:
    def __init__(self):
        self.token = environ['TOKEN']
        self.arenaList = []
        self.channel = ""
        self.checkinList = []
        self.competitionList = []
        self.gamePower = False
        self.number = 0
        self.minNumber = 1
        self.maxNumber = 1000000
        self.normalchannel = ""

    def main(self):
        intents = Intents.all()
        bot = commands.Bot(command_prefix="s!", intents=intents)

        def setchannel(self, bot):
            channel = bot.get_guild(772645756951724032).get_channel(958209445136064512)
            # channel = bot.get_guild(540408470504079361).get_channel(793664068057169940)
            return channel
        
        @bot.event
        async def on_ready():
            self.channel = setchannel(bot)
            print(f">> {bot.user.name} is ready")

        @bot.command(name = 'Clist', description = '報到名單', brief = '報到名單 (限定擁有管理權限)', pass_context=True)
        @has_permissions(manage_permissions=True, manage_channels=True)
        async def Clist(ctx):
            timer = 1
            str1 = ""
            for member in self.checkinList:
                str1 += f"<@{member}>, "
                if timer == 20:
                    await ctx.message.channel.send(str1)
            await ctx.message.channel.send(f"{str1}\n總共:{len(self.checkinList)}")

        @bot.command(name = 'checkin', description = '活動報到', brief = '活動報到', pass_context=True)
        async def checkin(ctx):
            if ctx.message.channel != 959800870776737842:
                return
            if self.gamePower:
                await ctx.message.channel.send("競賽已開始。")
                return
            member = ctx.message.author
            if str(member.id) in self.checkinList:
                await ctx.message.channel.send("已報到完成，請等待競賽開始。")
                return
            if ctx.message.guild.get_role(958018357515386930) in member.roles:
            # if ctx.message.guild.get_role(540408470504079361) in member.roles:
                self.checkinList.append(str(member.id))
                await ctx.message.channel.send("報到成功。")
            else:
                await ctx.message.channel.send("您並未報名參加本活動。")

        @bot.command(name = 'ci', description = '活動報到', brief = '活動報到', pass_context=True)
        async def ci(ctx):
            if ctx.message.channel != 959800870776737842:
                return
            if self.gamePower:
                await ctx.message.channel.send("競賽已開始。")
                return
            member = ctx.message.author
            if str(member.id) in self.checkinList:
                await ctx.message.channel.send("已報到完成，請等待競賽開始。")
                return
            if ctx.message.guild.get_role(958018357515386930) in member.roles:
            # if ctx.message.guild.get_role(540408470504079361) in member.roles:
                self.checkinList.append(str(member.id))
                await ctx.message.channel.send("報到成功。")
            else:
                await ctx.message.channel.send("您並未報名參加本活動。")

        # @bot.command(name = 'arena', description = '開啟對局 (一般場)', brief = '開啟對局 (一般場)', pass_context=True)
        # async def arena(ctx):
        #     if ctx.message.mentions == []:
        #         await ctx.channel.send("arena 使用方法:\n標記(tag)自己以及對手。")
        #         return

        #     if ctx.message.author not in ctx.message.mentions:
        #         await ctx.channel.send("必須包含自己在內。")
        #         return

        #     if len(ctx.message.mentions) != 2:
        #         await ctx.channel.send("最多人數 2。")
        #         return
            
        #     if self.gamePower:
        #         await ctx.message.channel.send(f"<@{ctx.message.author.id}>，正在執行競賽當中，請競賽結束後再做遊玩。")
        #         return

        #     for n in range(len(self.arenaList)):
        #         if ctx.message.author.id in self.arenaList[n]:
        #             await ctx.channel.send(f"<@{ctx.message.author.id}> 你已經設置比賽")
        #             return

        #     self.arenaList.append([ctx.message.mentions[0].id, 0, ctx.message.mentions[1].id, 0])
        #     await ctx.message.mentions[0].send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
        #     await ctx.message.mentions[1].send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
        #     await ctx.channel.send(f"<@{ctx.message.mentions[0].id}>, <@{ctx.message.mentions[1].id}> 作答已私訊，請私訊本機器人答案")
        #     self.normalchannel = ctx.channel

        @bot.command(name = 'match', description = '選手配對', brief = '選手配對 (限定擁有管理權限)', pass_context=True)
        @has_permissions(manage_permissions=True, manage_channels=True)
        async def match(ctx):
            if self.competitionList != []:
                await ctx.message.channel.send('比賽還未結束')
                return
            if self.arenaList != []:
                await ctx.message.channel.send('確定要開啟比賽，還有一般場尚未結束? (y/n/yes/no)')
                check = lambda m: m.author == ctx.author and m.channel == ctx.channel
                msg = await bot.wait_for('message', check=check, timeout=30)
                if msg.content == 'y' or msg.content == 'yes':
                    self.arenaList == []
                    self.gamePower = True
                    await ctx.message.channel.send('競賽已開啟')
                elif msg.content == 'n' or msg.content == 'no':
                    await ctx.message.channel.send('競賽已取消')
                    return
            # self.channel = ctx.channel
            # gc = pygsheets.authorize('client_secret.json')
            # sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1eIRcSbwYb0fpvvdBeVZfBlkMDhZV8x7S-KV-Z8wKS5U/')
            # wks = sht.worksheet_by_title("剪刀石頭布")
            # findList = wks.get_all_values(include_tailing_empty = False, include_tailing_empty_rows = False)
            if len(self.checkinList) <= 1:
                await ctx.message.channel.send("報名表是空白或只有一名參賽者，請確認是否有人報到!")
                return
            temp = []
            temp = self.checkinList
            self.competitionList = temp
            str1 = ""
            previous_player = ""
            if (len(self.competitionList)) % 2 == 1:
                random.shuffle(self.competitionList)
                try:
                    seedPlayer = self.competitionList[-1]
                    playcount = 1
                    for player in self.competitionList:
                        if playcount == 2:
                            self.arenaList.append([previous_player, 0, player, 0])
                        previous_player = player
                        playcount += 1
                    
                    countNum = 1
                    for arenalist in self.arenaList:
                        if countNum == 20:
                            str1 += f"<@{arenalist[0]}> vs <@{arenalist[2]}>\n"
                            await self.channel.send(f"{str1}")
                            str1 = ""
                        countNum += 1
                    await self.channel.send(f"{str1}")
                    await self.channel.send(f"種子選手為 <@{seedPlayer}>")
                except KeyError:
                    await ctx.message.channel.send('最後一位為種子選手')
            else:
                random.shuffle(self.competitionList)
                try:
                    playcount = 1
                    for player in self.competitionList:
                        if playcount == 2:
                            self.arenaList.append([previous_player, 0, player, 0])
                        previous_player = player
                        playcount += 1
                    
                    countNum = 1
                    for arenalist in self.arenaList:
                        if countNum == 20:
                            str1 += f"<@{arenalist[0]}> vs <@{arenalist[2]}>\n"
                            await self.channel.send(f"{str1}")
                            str1 = ""
                        countNum += 1
                    await self.channel.send(f"{str1}")
                except KeyError:
                    await ctx.message.channel.send('最後一位為種子選手')

        @bot.command(name = 'open', description = '開始比賽', brief = '開始配對後的對局 (限定擁有管理權限)', pass_context=True)
        @has_permissions(manage_permissions=True, manage_channels=True)
        async def open(ctx):
            if self.arenaList == []:
                await ctx.message.channel.send("尚未擁有對局。")
                return
            await ctx.message.channel.send("對局將依序開始，請私訊本機器人作答。")
            for index in range(len(self.arenaList)):
                await ctx.guild.get_member(int(self.arenaList[0][0])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                await ctx.guild.get_member(int(self.arenaList[0][2])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')

        @bot.command(name = 'nm', description = '下個賽程', brief = '下個賽程/下一局 (限定擁有管理權限)', pass_context=True)
        @has_permissions(manage_permissions=True, manage_channels=True)
        async def nm(ctx):
            if self.arenaList != []:
                await ctx.message.channel.send(f"還有對局尚未完成!")
                await ctx.message.channel.send('確定要進行下局比賽，尚未完成比賽的將會取消資格? (y/n/yes/no)')
                try:
                    check = lambda m: m.author == ctx.author and m.channel == ctx.channel
                    msg = await bot.wait_for('message', check=check, timeout=30)
                    if msg.content == 'y' or msg.content == 'yes':
                        for arenaLis in self.arenaList:
                            if arenaLis[1] == 0:
                                self.competitionList.remove(arenaLis[0])
                            if arenaLis[3] == 0:
                                self.competitionList.remove(arenaLis[2])
                        self.arenaList = []
                        await ctx.message.channel.send('對局已清空，將進行下一局比賽。')
                    elif msg.content == 'n' or msg.content == 'no':
                        await ctx.message.channel.send('已取消。')
                        return
                except:
                    await ctx.message.channel.send('時間到。')
                    return
            str1 = ""
            temp = []
            if len(self.competitionList) == 1:
                await self.channel.send(f"👑 <@{self.competitionList[0]}> 為本次**冠軍**")
                self.gamePower = False
                self.competitionList = []
                return
            if (len(self.competitionList)) % 2 == 1:
                random.shuffle(self.competitionList)
                try:
                    seedPlayer = self.competitionList[-1]
                    playcount = 1
                    for player in self.competitionList:
                        if playcount == 2:
                            self.arenaList.append([previous_player, 0, player, 0])
                        previous_player = player
                        playcount += 1
                    
                    countNum = 1
                    for arenalist in self.arenaList:
                        if countNum == 20:
                            str1 += f"<@{arenalist[0]}> vs <@{arenalist[2]}>\n"
                            await self.channel.send(f"{str1}")
                            str1 = ""
                        countNum += 1
                    await self.channel.send(f"{str1}")
                    await self.channel.send(f"種子選手為 <@{seedPlayer}>")
                except KeyError:
                    await ctx.message.channel.send('最後一位為種子選手')
            else:
                random.shuffle(self.competitionList)
                try:
                    playcount = 1
                    for player in self.competitionList:
                        if playcount == 2:
                            self.arenaList.append([previous_player, 0, player, 0])
                        previous_player = player
                        playcount += 1
                    
                    countNum = 1
                    for arenalist in self.arenaList:
                        if countNum == 20:
                            str1 += f"<@{arenalist[0]}> vs <@{arenalist[2]}>\n"
                            await self.channel.send(f"{str1}")
                            str1 = ""
                        countNum += 1
                    await self.channel.send(f"{str1}")
                except KeyError:
                    await ctx.message.channel.send('最後一位為種子選手')

        @bot.command(name = 'stop', description = '停止對局 (一般場)', brief = '停止對局 (一般場)', pass_context=True)
        async def stop(ctx):
            if self.gamePower:
                await ctx.message.channel.send('競賽無法自己停止對局。')
                return
            for index in range(len(self.arenaList)):
                if ctx.message.author.id in self.arenaList[index]:
                    await ctx.message.channel.send('確定要取消? (y/n/yes/no)')
                    check = lambda m: m.author == ctx.author and m.channel == ctx.channel
                    msg = await bot.wait_for('message', check=check, timeout=30)
                    if msg.content == 'y' or msg.content == 'yes':
                        self.arenaList.remove(self.arenaList[index])
                        await ctx.message.channel.send('對局已終止')
                        return
                    elif msg.content == 'n' or msg.content == 'no':
                        await ctx.message.channel.send('指令已取消')
                        return
            await ctx.message.channel.send("尚未開啟對局。")

        @bot.command(name = 'Cstop', description = '取消賽程', brief = '取消賽程 (限定擁有管理權限)', pass_context=True)
        @has_permissions(manage_permissions=True, manage_channels=True)
        async def Cstop(ctx):
            if self.competitionList != []:
                await ctx.message.channel.send('確定要取消? (y/n/yes/no)')
                check = lambda m: m.author == ctx.author and m.channel == ctx.channel
                msg = await bot.wait_for('message', check=check, timeout=30)
                if msg.content == 'y' or msg.content == 'yes':
                    self.competitionList == []
                    self.checkinList = []
                    self.gamePower = False
                    await ctx.message.channel.send('競賽已終止')
                elif msg.content == 'n' or msg.content == 'no':
                    await ctx.message.channel.send('指令已取消')

        @bot.command(name = 'as', description = '目前剩餘對局', brief = '目前剩餘對局 (限定擁有管理權限)', pass_context=True)
        @has_permissions(manage_permissions=True, manage_channels=True)
        async def status(ctx):
            if not(self.gamePower):
                str1 = "目前一般場對局名單:\n"
                for lis in self.arenaList:
                    str1 += f"<@{lis[0]}> 和 <@{lis[2]}>\n"
                await ctx.message.channel.send(str1)
                return
            if self.arenaList == []:
                await ctx.message.channel.send("目前已無對局。")
                return
            str1 = "目前競賽剩餘對局名單:\n"
            for lis in self.arenaList:
                str1 += f"<@{lis[0]}> 和 <@{lis[2]}>\n"
            await ctx.message.channel.send(str1)

        @bot.event
        async def on_message(message):
            if message is None:
                return
            if message.guild is None:
                try:
                    if message.author.bot:
                        if not "embed" in message.content:
                            return
                    if len(self.arenaList) == 0:
                        return
                    if message.author.id in self.arenaList[0] or str(message.author.id) in self.arenaList[0]:
                        if message.content == '1' or message.content == '2' or message.content == '3':
                            await message.author.send(f'你選擇 : {message.content}')
                            index = self.arenaList[0].index(str(message.author.id))
                            self.arenaList[0][index+1] = int(message.content)
                            if self.arenaList[0][1] != 0 and self.arenaList[0][3] != 0:
                                if self.arenaList[0][1] == 1 and self.arenaList[0][3] == 2:
                                    if self.gamePower:
                                        await self.channel.send(f"<@{self.arenaList[0][0]}> 出剪刀 vs <@{self.arenaList[0][2]}> 出石頭\n★ <@{self.arenaList[0][2]}> 獲勝")
                                    else:
                                        await self.normalchannel.send(f"<@{self.arenaList[0][0]}> 出剪刀 vs <@{self.arenaList[0][2]}> 出石頭\n★ <@{self.arenaList[0][2]}> 獲勝")
                                    if self.competitionList != []:
                                        try: 
                                            self.competitionList.remove(f'{self.arenaList[0][0]}')
                                        except Exception as e:
                                            pass
                                    self.arenaList.remove(self.arenaList[0])
                                    await self.channel.guild.get_member(int(self.arenaList[0][0])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                    await self.channel.guild.get_member(int(self.arenaList[0][2])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                elif self.arenaList[0][1] == 2 and self.arenaList[0][3] == 3:
                                    if self.gamePower:
                                        await self.channel.send(f"<@{self.arenaList[0][0]}> 出石頭 vs <@{self.arenaList[0][2]}> 出布\n★ <@{self.arenaList[0][2]}> 獲勝")
                                    else:
                                        await self.normalchannel.send(f"<@{self.arenaList[0][0]}> 出石頭 vs <@{self.arenaList[0][2]}> 出布\n★ <@{self.arenaList[0][2]}> 獲勝")
                                    if self.competitionList != []:
                                        try: 
                                            self.competitionList.remove(f'{self.arenaList[0][0]}')
                                        except Exception as e:
                                            pass
                                    self.arenaList.remove(self.arenaList[0])
                                    await self.channel.guild.get_member(int(self.arenaList[0][0])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                    await self.channel.guild.get_member(int(self.arenaList[0][2])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                elif self.arenaList[0][1] == 3 and self.arenaList[0][3] == 1:
                                    if self.gamePower:
                                        await self.channel.send(f"<@{self.arenaList[0][0]}> 出布 vs <@{self.arenaList[0][2]}> 出剪刀\n★ <@{self.arenaList[0][2]}> 獲勝")
                                    else:
                                        await self.normalchannel.send(f"<@{self.arenaList[0][0]}> 出布 vs <@{self.arenaList[0][2]}> 出剪刀\n★ <@{self.arenaList[0][2]}> 獲勝")
                                    if self.competitionList != []:
                                        try: 
                                            self.competitionList.remove(f'{self.arenaList[0][0]}')
                                        except Exception as e:
                                            pass
                                    self.arenaList.remove(self.arenaList[0])
                                    await self.channel.guild.get_member(int(self.arenaList[0][0])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                    await self.channel.guild.get_member(int(self.arenaList[0][2])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                elif self.arenaList[0][1] == 2 and self.arenaList[0][3] == 1:
                                    if self.gamePower:
                                        await self.channel.send(f"<@{self.arenaList[0][0]}> 出石頭 vs <@{self.arenaList[0][2]}> 出剪刀\n★ <@{self.arenaList[0][0]}> 獲勝")
                                    else:
                                        await self.normalchannel.send(f"<@{self.arenaList[0][0]}> 出石頭 vs <@{n[2]}> 出剪刀\n★ <@{self.arenaList[0][0]}> 獲勝")
                                    if self.competitionList != []:
                                        try: 
                                            self.competitionList.remove(f'{self.arenaList[0][2]}')
                                        except Exception as e:
                                            pass
                                    self.arenaList.remove(self.arenaList[0])
                                    await self.channel.guild.get_member(int(self.arenaList[0][0])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                    await self.channel.guild.get_member(int(self.arenaList[0][2])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                elif self.arenaList[0][1] == 3 and self.arenaList[0][3] == 2:
                                    if self.gamePower:
                                        await self.channel.send(f"<@{self.arenaList[0][0]}> 出布 vs <@{self.arenaList[0][2]}> 出石頭\n★ <@{self.arenaList[0][0]}> 獲勝")
                                    else:
                                        await self.normalchannel.send(f"<@{self.arenaList[0][0]}> 出布 vs <@{self.arenaList[0][2]}> 出石頭\n★ <@{self.arenaList[0][0]}> 獲勝")
                                    if self.competitionList != []:
                                        try: 
                                            self.competitionList.remove(f'{self.arenaList[0][2]}')
                                        except Exception as e:
                                            pass
                                    self.arenaList.remove(self.arenaList[0])
                                    await self.channel.guild.get_member(int(self.arenaList[0][0])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                    await self.channel.guild.get_member(int(self.arenaList[0][2])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                elif self.arenaList[0][1] == 1 and self.arenaList[0][3] == 3:
                                    if self.gamePower:
                                        await self.channel.send(f"<@{self.arenaList[0][0]}> 出剪刀 vs <@{self.arenaList[0][2]}> 出布\n★ <@{self.arenaList[0][0]}> 獲勝")
                                    else:
                                        await self.normalchannel.send(f"<@{self.arenaList[0][0]}> 出剪刀 vs <@{self.arenaList[0][2]}> 出布\n★ <@{self.arenaList[0][0]}> 獲勝")
                                    if self.competitionList != []:
                                        try: 
                                            self.competitionList.remove(f'{self.arenaList[0][2]}')
                                        except Exception as e:
                                            pass
                                    self.arenaList.remove(self.arenaList[0])
                                    await self.channel.guild.get_member(int(self.arenaList[0][0])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                    await self.channel.guild.get_member(int(self.arenaList[0][2])).send(f'請選擇 : \n1. 剪刀(輸入1/type 1)\n2. 石頭(輸入2/type 2)\n3. 布(輸入3/type 3)')
                                else:
                                    if self.arenaList[0][1] == self.arenaList[0][3] and self.arenaList[0][1] == 1:
                                        # await self.channel.send(f"<@{self.arenaList[n][0]}> 出剪刀 vs <@{self.arenaList[n][2]}> 出剪刀\n 平手\n請繼續私訊作答")
                                        await self.channel.guild.get_member(int(self.arenaList[0][0])).send(f"◆ 平手\n請繼續作答")
                                        await self.channel.guild.get_member(int(self.arenaList[0][2])).send(f"◆ 平手\n請繼續作答")
                                    elif self.arenaList[0][1] == self.arenaList[0][3] and self.arenaList[0][1] == 2:
                                        # await self.channel.send(f"<@{self.arenaList[n][0]}> 出石頭 vs <@{self.arenaList[n][2]}> 出石頭\n 平手\n請繼續私訊作答")
                                        await self.channel.guild.get_member(int(self.arenaList[0][0])).send(f"◆ 平手\n請繼續作答")
                                        await self.channel.guild.get_member(int(self.arenaList[0][2])).send(f"◆ 平手\n請繼續作答")
                                    elif self.arenaList[0][1] == self.arenaList[0][3] and self.arenaList[0][1] == 3:
                                        # await self.channel.send(f"<@{self.arenaList[n][0]}> 出布 vs <@{self.arenaList[n][2]}> 出布\n 平手\n請繼續私訊作答")
                                        await self.channel.guild.get_member(int(self.arenaList[0][0])).send(f"◆ 平手\n請繼續作答")
                                        await self.channel.guild.get_member(int(self.arenaList[0][2])).send(f"◆ 平手\n請繼續作答")
                                    self.arenaList[0][1] = 0
                                    self.arenaList[0][3] = 0
                                
                                if len(self.competitionList) == 1:
                                    await self.channel.send(f"👑 <@{self.competitionList[0]}> 為本次**冠軍**")
                                    self.gamePower = False
                                    self.competitionList = []
                                    self.checkinList = []
                                
                                if len(self.arenaList) == 0:
                                    await self.channel.send(f"全部對局已結束，請管理員進行下一局配對。")
                                elif len(self.arenaList) > 0:
                                    await self.channel.send(f"請下一組進行對局。\n<@{self.arenaList[0][0]}>, <@{self.arenaList[0][2]}>")
                        else:
                            await message.author.send("請選擇正確數字")
                            return
                except Exception as e:
                    print(f"On Message Error: {e}")
                            
            await bot.process_commands(message)

        @bot.command(name = 'n', description = '輸入數字', brief = '輸入數字', pass_context=True)
        async def number(ctx, arg):
            if self.number == 0:
                await ctx.message.channel.send("尚未設定數字。")
                return
            try:
                if int(arg) > self.number:
                    if int(arg) > self.maxNumber:
                        await ctx.message.channel.send(f"<@{ctx.message.author.id}>, 請輸入範圍 : {self.minNumber} 到 {self.maxNumber} 的數字")
                        return
                    if self.maxNumber - int(arg) > 2000:
                        await ctx.message.channel.send(f"<@{ctx.message.author.id}>, 請輸入與最大最小值相差2000內的數字。")
                        return
                    self.maxNumber = int(arg)
                    await ctx.message.channel.send(f"範圍 : {self.minNumber} 到 {self.maxNumber}")
                elif int(arg) < self.number:
                    if int(arg) < self.minNumber:
                        await ctx.message.channel.send(f"<@{ctx.message.author.id}>, 請輸入範圍 : {self.minNumber} 到 {self.maxNumber} 的數字")
                        return
                    if int(arg) - self.minNumber > 2000:
                        await ctx.message.channel.send(f"<@{ctx.message.author.id}>, 請輸入與最大最小值相差2000內的數字。")
                        return
                    self.minNumber = int(arg)
                    await ctx.message.channel.send(f"範圍 : {self.minNumber} 到 {self.maxNumber}")
                elif int(arg) == self.number:
                    await ctx.message.channel.send(f"恭喜 <@{ctx.message.author.id}> 猜到正確數字 {self.number}")
                    self.number = 0
            except:
                await ctx.message.channel.send(f"<@{ctx.message.author.id}>, 輸入錯誤。")

        @bot.command(name = 'cn', description = '產生數字', brief = '產生數字', pass_context=True)
        @has_permissions(manage_permissions=True, manage_channels=True)
        async def create_Number(ctx):
            if self.number != 0:
                await ctx.message.channel.send("比賽尚未結束!")
                return
            self.number = random.choice(range(1,1000001))
            await ctx.message.channel.send("數字設置完成，猜數字開始!")


        bot.run(self.token)

if __name__ == "__main__":
    print("Hello World!")
    # bot = shiinaBot()
    # bot.main()
