import discord
import random
import ast
from discord.ext import commands
import datetime
from discord.commands import Option

bot = discord.Bot(intents=discord.Intents.all(), owner_id=1015942852582326292)

roleemojis = [
    "<:initiator:1159498006039629894>",  # 척후대
    "<:duelist:1159498003418206278>",  # 타격대
    "<:sentinel:1159498007591538688>",  # 감시자
    "<:controller:1159498001891467364>",  # 전략가
]
mapimgs = {
    "로터스": "https://cdn.discordapp.com/attachments/1159496780136849472/1159499423710195752/687ccd6f515be17b.webp",
    "바인드": "https://cdn.discordapp.com/attachments/1159496780136849472/1159499428881776762/56c737a20d17c431.webp",
    "브리즈": "https://cdn.discordapp.com/attachments/1159496780136849472/1159499433789112340/9ae19cd9a8edddb5.webp",
    "선셋": "https://cdn.discordapp.com/attachments/1159496780136849472/1159499441213022348/aacb1f965cc25b25.webp",
    "스플릿": "https://cdn.discordapp.com/attachments/1159496780136849472/1159499447613542480/a6f62ed9370596da.webp",
    "아이스박스": "https://cdn.discordapp.com/attachments/1159496780136849472/1159499452910940290/b2da601a1fe7b605.webp",
    "어센트": "https://cdn.discordapp.com/attachments/1159496780136849472/1159499460712353902/1aa4b547bc441703.webp",
    "펄": "https://cdn.discordapp.com/attachments/1159496780136849472/1159499469021257859/1da2274df9d8ee91.webp",
    "프랙처": "https://cdn.discordapp.com/attachments/1159496780136849472/1159499473773404220/793aad2477894df4.webp",
    "헤이븐": "https://media.discordapp.net/attachments/1159496780136849472/1159499479536369754/60f40e9053aa8904.webp",
}
gunimgs = {
    "오딘": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496895526346855/f40f9f4cfb6ba714.webp",
    "아레스": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496899011813486/444f0fd3628b093b.webp",
    "오퍼레이터": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496900832149614/202698ea90306ecf.webp",
    "마샬": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496902862180412/94eeec87dd1a4f96.webp",
    "팬텀": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496904590245970/1eb1c69368ca75f0.webp",
    "밴달": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496906356031488/bf3d6bc12ab1631e.webp",
    "가디언": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496908365123604/ac6b950adce7b907.webp",
    "불독": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496927004606515/4ae45b6079a661bf.webp",
    "저지": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496928644575353/a056f63266d7e815.webp",
    "버키": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496930389405716/9540a32b0fd8ae8d.webp",
    "스펙터": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496860092862474/fef2c503f13e2303.webp",
    "스팅어": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496862252945428/3f45d7b4e40c5d44.webp",
    "셰리프": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496864119398521/6cf27cb5c0170958.webp",
    "고스트": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496866065567786/227d305cf85a0186.webp",
    "프렌지": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496867760054313/ffccf92973e1cf3a.webp",
    "쇼티": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496869400035460/5dd5806631cf8670.webp",
    "클래식": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496871484600361/593b7f4f53d2d82c.webp",
    "칼": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496891709526036/4f75a4d3e1026449.webp",
}
agentimgs = {
    "아스트라": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496933493198958/db3c9d9b11664522.webp",
    "바이퍼": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496935460306985/059836713363a75b.webp=",
    "케이오": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496937704280194/c8bc0291dfff8843.webp",
    "사이퍼": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496940300546150/8ac03789c94bd388.webp",
    "게코": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496941953101894/5cf9a40477fdef2e.webp",
    "세이지": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496962102546492/333606286b1d906a.webp",
    "소바": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496966720458812/390c48c3cfddfc58.webp",
    "하버": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496972445691954/7988afbae00a7b1f.webp",
    "스카이": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496977898278912/69dd50118c7354c8.webp",
    "브림스톤": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496981803188326/2e362286ac3952d2.webp",
    "요루": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496987654226051/f746ede4314f4e84.webp",
    "브리치": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496992511242460/b37ad4fe4695abfb.webp",
    "오멘": "https://cdn.discordapp.com/attachments/1159496780136849472/1159496997867376702/4e2a62e511740603.webp",
    "킬조이": "https://cdn.discordapp.com/attachments/1159496780136849472/1159497005098340413/e16220cd6824e395.webp",
    "데드록": "https://cdn.discordapp.com/attachments/1159496780136849472/1159497009351381082/5980119f0638cff2.webp",
    "페이드": "https://cdn.discordapp.com/attachments/1159496780136849472/1159497017140187217/b0f2edff78116985.webp",
    "체임버": "https://cdn.discordapp.com/attachments/1159496780136849472/1159497023494553710/64002411139f5914.webp",
    "네온": "https://cdn.discordapp.com/attachments/1159496780136849472/1159497028989100134/493b642b412f7901.webp",
    "레이나": "https://cdn.discordapp.com/attachments/1159496780136849472/1159497033749639258/a7575105067c6108.webp",
    "레이즈": "https://cdn.discordapp.com/attachments/1159496780136849472/1159497039244177418/2468c6d67e4f820c.webp",
    "제트": "https://cdn.discordapp.com/attachments/1159496780136849472/1159497044822589490/1fc7dd19ab9a4889.webp",
    "피닉스": "https://cdn.discordapp.com/attachments/1159496780136849472/1159497049763479632/586749533bb4a6ae.webp",
}
agentcategory = {
    "척후대": "케이오/게코/소바/스카이/브리치/페이드".split("/"),
    "타격대": "요루/네온/레이나/레이즈/제트/피닉스".split("/"),
    "감시자": "사이퍼/세이지/킬조이/데드록/체임버".split("/"),
    "전략가": "아스트라/바이퍼/하버/브림스톤/오멘".split("/"),
}
agentcategoryimgs = {
    "척후대": "https://cdn.discordapp.com/emojis/1159498006039629894.webp",
    "타격대": "https://cdn.discordapp.com/emojis/1159498003418206278.webp",
    "감시자": "https://cdn.discordapp.com/emojis/1159498007591538688.webp",
    "전략가": "https://cdn.discordapp.com/emojis/1159498001891467364.webp",
}


@bot.event
async def on_ready():
    print("ready")
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game("Valorant Helper Running")
    )


class AgentCategoryView(discord.ui.View):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.start = [i for i in self.children if i.label == "뽑기"][0]
        self.role_buttons = [i for i in self.children if i.row == 0]
        self.roles = [True, True, True, True]  # 척후대, 타격대, 감시자, 전략가

    async def check(self, interaction):
        if self.roles == [False, False, False, False]:
            if not self.start.disabled:
                self.start.disabled = True
        else:
            if self.start.disabled:
                self.start.disabled = False
        await interaction.response.edit_message(view=self)

    async def change_label(self, button, role):
        button.label = button.label[:-2] + ("추가" if self.roles[role] else "제거")
        button.style = (
            discord.ButtonStyle.green
            if self.roles[role]
            else discord.ButtonStyle.danger
        )
        self.roles[role] = not self.roles[role]

    @discord.ui.button(
        label="척후대 제거", style=discord.ButtonStyle.danger, emoji=roleemojis[0], row=0
    )
    async def initiators(self, button, interaction):
        await self.change_label(button, 0)
        await self.check(interaction)

    @discord.ui.button(
        label="타격대 제거", style=discord.ButtonStyle.danger, emoji=roleemojis[1], row=0
    )
    async def duelists(self, button, interaction):
        await self.change_label(button, 1)
        await self.check(interaction)

    @discord.ui.button(
        label="감시자 제거", style=discord.ButtonStyle.danger, emoji=roleemojis[2], row=0
    )
    async def sentinels(self, button, interaction):
        await self.change_label(button, 2)
        await self.check(interaction)

    @discord.ui.button(
        label="전략가 제거", style=discord.ButtonStyle.danger, emoji=roleemojis[3], row=0
    )
    async def controllers(self, button, interaction):
        await self.change_label(button, 3)
        await self.check(interaction)

    @discord.ui.button(label="전체 추가", style=discord.ButtonStyle.green, row=1)
    async def add_entire(self, button, interaction):
        for i in range(4):
            self.role_buttons[i].label = self.role_buttons[i].label[:-2] + "제거"
            self.role_buttons[i].style = discord.ButtonStyle.danger
        self.roles = [True, True, True, True]
        await self.check(interaction)

    @discord.ui.button(label="전체 제거", style=discord.ButtonStyle.danger, row=1)
    async def remove_entire(self, button, interaction):
        for i in range(4):
            self.role_buttons[i].label = self.role_buttons[i].label[:-2] + "추가"
            self.role_buttons[i].style = discord.ButtonStyle.green
        self.roles = [False, False, False, False]
        await self.check(interaction)

    @discord.ui.button(label="뽑기", row=1, style=discord.ButtonStyle.blurple)
    async def choice(self, button, interaction):
        agents = []
        if self.roles[0]:
            agents.extend(agentcategory["척후대"])
        if self.roles[1]:
            agents.extend(agentcategory["타격대"])
        if self.roles[2]:
            agents.extend(agentcategory["감시자"])
        if self.roles[3]:
            agents.extend(agentcategory["전략가"])
        agent = random.choice(agents)
        category = [i for i in agentcategory.keys() if agent in agentcategory[i]][0]
        embed = discord.Embed(
            title="요원 뽑기 결과",
            description="**" + agent + "**",
            color=0x00FFFF,
            timestamp=datetime.datetime.now(),
        )
        embed.set_thumbnail(url=agentcategoryimgs[category])
        embed.set_image(url=agentimgs[agent])
        await interaction.message.edit(embed=embed, view=None)


@bot.slash_command(name="요원뽑기")
async def choiceAgent(ctx: discord.ApplicationContext):
    await ctx.respond(view=AgentCategoryView(ctx))


mapsgroup = bot.create_group("맵", "맵 뽑기 관련 명령어")
maps = "스플릿/바인드/헤이븐/어센트/아이스박스/브리즈/프랙처/펄/로터스/선셋".split("/")


@mapsgroup.command(name="뽑기")
async def randommap(ctx: discord.ApplicationContext):
    m = random.choice(maps)
    embed = discord.Embed(
        title="맵 뽑기 결과",
        description="**" + m + "**",
        color=0x00FFFF,
        timestamp=datetime.datetime.now(),
    )
    embed.set_image(url=mapimgs[m])
    await ctx.respond(embed=embed)


@mapsgroup.command(name="제거")
async def removemap(ctx: discord.ApplicationContext, 제거할맵: str):
    mapstoremove = 제거할맵.split("/")
    for i in mapstoremove:
        del maps[maps.index(i)]
    embed = discord.Embed(
        title="맵 제거 완료", color=0x00FFFF, timestamp=datetime.datetime.now()
    )
    embed.add_field(
        name="제거된 맵", value="**" + "**, **".join(mapstoremove) + "**", inline=False
    )
    embed.add_field(
        name="현재 맵 목록", value="**" + "**, **".join(maps) + "**", inline=False
    )
    await ctx.respond(embed=embed)


@mapsgroup.command(name="추가")
async def addmap(ctx: discord.ApplicationContext, 추가할맵: str):
    mapstoadd = 추가할맵.split("/")
    maps.extend(mapstoadd)
    embed = discord.Embed(
        title="맵 추가 완료", color=0x00FFFF, timestamp=datetime.datetime.now()
    )
    embed.add_field(
        name="추가된 맵", value="**" + "**, **".join(mapstoadd) + "**", inline=False
    )
    embed.add_field(
        name="현재 맵 목록", value="**" + "**, **".join(maps) + "**", inline=False
    )
    await ctx.respond(embed=embed)


@mapsgroup.command(name="리셋")
async def resetmap(ctx: discord.ApplicationContext):
    maps = "스플릿/바인드/헤이븐/어센트/아이스박스/브리즈/프랙처/펄/로터스/선셋".split("/")
    embed = discord.Embed(
        title="리셋 완료", color=0x00FFFF, timestamp=datetime.datetime.now()
    )
    await ctx.respond(embed=embed)


@mapsgroup.command(name="목록")
async def listmap(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        title="맵 목록",
        description="**" + "**, **".join(maps) + "**",
        color=0x00FFFF,
        timestamp=datetime.datetime.now(),
    )
    await ctx.respond(embed=embed)


@bot.slash_command(name="팀원뽑기")
async def choiceTeam(
    ctx: discord.ApplicationContext,
    팀원수: Option(int, "A팀의 팀원 수", required=False, default=0),
):
    people = [i.id for i in ctx.author.voice.channel.members]
    number = 팀원수 or len(people) // 2
    a = []
    while len(a) < number:
        a.append(random.choice(people))
        del people[people.index(a[-1])]
    embed = discord.Embed(
        title="팀원 뽑기 결과", color=0x00FFFF, timestamp=datetime.datetime.now()
    )
    embed.add_field(
        name="A팀", value=", ".join(["<@" + str(i) + ">" for i in people]), inline=False
    )
    embed.add_field(
        name="B팀", value=", ".join(["<@" + str(i) + ">" for i in a]), inline=False
    )
    await ctx.respond(embed=embed)


@bot.slash_command(name="모드뽑기")
async def randommap(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        title="모드 뽑기 결과",
        description="**"
        + random.choice("일반전/경쟁전/스파이크 돌격/신속플레이/데스매치/팀 데스매치/에스컬레이션".split("/"))
        + "**",
        color=0x00FFFF,
        timestamp=datetime.datetime.now(),
    )
    await ctx.respond(embed=embed)


class GunCategoryView(discord.ui.View):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx

    @discord.ui.select(
        placeholder="총 종류",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="보조 무기", description="권총들+칼"),
            discord.SelectOption(label="주 무기", description="권총 빼고 나머지+칼"),
            discord.SelectOption(label="모두", description="모든 무기"),
        ],
    )
    async def select_callback(self, select, interaction):
        if interaction.user.id != self.ctx.author.id:
            return
        mode = select.values[0]
        guns = ["칼"]
        if mode == "보조 무기" or mode == "모두":
            guns.extend("클래식/쇼티/프렌지/고스트/셰리프".split("/"))
        if mode == "주 무기" or mode == "모두":
            guns.extend("스팅어/스펙터/버키/저지/불독/가디언/팬텀/밴달/마샬/오퍼레이터/아레스/오딘".split("/"))
        gun = random.choice(guns)
        embed = discord.Embed(
            title="총 뽑기 결과",
            description="**" + gun + "**",
            color=0x00FFFF,
            timestamp=datetime.datetime.now(),
        )
        embed.set_image(url=gunimgs[gun])
        await interaction.message.edit(embed=embed, view=None)


@bot.slash_command(name="총뽑기")
async def choiceGun(ctx: discord.ApplicationContext):
    await ctx.respond(view=GunCategoryView(ctx))


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


class CodeModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(
            discord.ui.InputText(label="Code", style=discord.InputTextStyle.long)
        )

    def setctx(self, ctx):
        self.ctx = ctx

    async def callback(self, interaction: discord.Interaction):
        fn_name = "_eval_expr"
        env = {
            "bot": bot,
            "discord": discord,
            "ctx": self.ctx,
            "__import__": __import__,
        }
        cmd = self.children[0].value

        parsed_stmts = ast.parse(cmd)

        fn_name = "_eval_expr"

        fn = f"async def {fn_name}(): pass"
        parsed_fn = ast.parse(fn)

        for node in parsed_stmts.body:
            ast.increment_lineno(node)

        insert_returns(parsed_stmts.body)

        parsed_fn.body[0].body = parsed_stmts.body
        exec(compile(parsed_fn, filename="<ast>", mode="exec"), env)

        await interaction.response.send_message(
            "```\n" + str(await eval(f"{fn_name}()", env)) + "```", ephemeral=True
        )


@bot.slash_command(name="eval")
async def evalfn(ctx: discord.ApplicationContext):
    if ctx.author.id != bot.owner_id:
        return await ctx.respond("개발자 전용", ephemeral=True)
    modal = CodeModal(title="Code")
    modal.setctx(ctx)
    await ctx.send_modal(modal)


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel == after.channel and before.channel is not None:
        return
    if before.channel is not None:
        if len(before.channel.members) == 0 and (
            before.channel.name.startswith("게임-")
            or before.channel.name.startswith("노래방-")
        ):
            await before.channel.delete()
    if after.channel is not None:
        if after.channel.id == 1159491194292801607:
            channel = await bot.get_channel(1159495333219401850).create_voice_channel(
                "게임-" + member.name
            )
            await member.move_to(channel)
        elif after.channel.id == 1159504725314633859:
            channel = await bot.get_channel(1159495333219401850).create_voice_channel(
                "노래방-" + member.name
            )


bot.run(open("token.txt").read())
