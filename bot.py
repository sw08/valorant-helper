import discord
import random
import ast
from discord.ext import commands
import datetime
from discord.commands import Option

bot = discord.Bot(intents=discord.Intents.all(), owner_id=1015942852582326292)
mapimgs = {
    '로터스': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845536309846106/687ccd6f515be17b.webp',
    '바인드': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845536553107467/56c737a20d17c431.webp',
    '브리즈': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845537186463824/9ae19cd9a8edddb5.webp',
    '선셋': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845537559748618/aacb1f965cc25b25.webp',
    '스플릿': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845537987559494/a6f62ed9370596da.webp',
    '아이스박스': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845538423775302/b2da601a1fe7b605.webp',
    '어센트': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845538700591174/1aa4b547bc441703.webp',
    '펄': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845539367501884/1da2274df9d8ee91.webp',
    '프랙처': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845539891781763/793aad2477894df4.webp',
    '헤이븐': 'https://cdn.discordapp.com/attachments/836864790294298654/1147845540336369684/60f40e9053aa8904.webp'
}
gunimgs = {
    '오딘': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064025556754544/f40f9f4cfb6ba714.webp',
    '아레스': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064025879724062/444f0fd3628b093b.webp',
    '오퍼레이터': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064026122977393/202698ea90306ecf.webp',
    '마샬': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064026378838026/94eeec87dd1a4f96.webp',
    '팬텀': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064026647281674/1eb1c69368ca75f0.webp',
    '밴달': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064026966032454/bf3d6bc12ab1631e.webp',
    '가디언': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064027205116037/ac6b950adce7b907.webp',
    '불독': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064027528085677/4ae45b6079a661bf.webp',
    '저지': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064027767144509/a056f63266d7e815.webp',
    '버키': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064027985256589/9540a32b0fd8ae8d.webp',
    '스펙터': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064090056761404/fef2c503f13e2303.webp',
    '스팅어': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064090589450320/3f45d7b4e40c5d44.webp',
    '셰리프': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064091151466636/6cf27cb5c0170958.webp',
    '고스트': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064091470241922/227d305cf85a0186.webp',
    '프렌지': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064091830943744/ffccf92973e1cf3a.webp',
    '쇼티': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064092170690580/5dd5806631cf8670.webp',
    '클래식': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064092464304188/593b7f4f53d2d82c.webp',
    '칼': 'https://cdn.discordapp.com/attachments/836864790294298654/1150064092728533012/4f75a4d3e1026449.webp' 
}

mapsgroup = bot.create_group('맵', '맵 뽑기 관련 명령어')
maps = '스플릿/바인드/헤이븐/어센트/아이스박스/브리즈/프랙처/펄/로터스/선셋'.split('/')

@bot.event
async def on_ready():
    print('ready')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Valorant Helper Running'))

@mapsgroup.command(name='뽑기')
async def randommap(ctx: discord.ApplicationContext):
    m = random.choice(maps)
    embed = discord.Embed(title='맵 뽑기 결과', description='**' + m + '**', color=0x00ffff, timestamp=datetime.datetime.now())
    embed.set_image(url=mapimgs[m])
    await ctx.respond(embed=embed)

@mapsgroup.command(name='제거')
async def removemap(ctx: discord.ApplicationContext, 제거할맵: str):
    mapstoremove = 제거할맵.split('/')
    for i in mapstoremove:
        del maps[maps.index(i)]
    embed = discord.Embed(title='맵 제거 완료', color=0x00ffff, timestamp=datetime.datetime.now())
    embed.add_field(name='제거된 맵', value='**' + '**, **'.join(mapstoremove) + '**', inline=False)
    embed.add_field(name='현재 맵 목록', value='**' + '**, **'.join(maps) + '**', inline=False)
    await ctx.respond(embed=embed)

@mapsgroup.command(name='추가')
async def addmap(ctx: discord.ApplicationContext, 추가할맵: str):
    mapstoadd = 추가할맵.split('/')
    maps.extend(mapstoadd)
    embed = discord.Embed(title='맵 추가 완료', color=0x00ffff, timestamp=datetime.datetime.now())
    embed.add_field(name='추가된 맵', value='**' + '**, **'.join(mapstoadd) + '**', inline=False)
    embed.add_field(name='현재 맵 목록', value='**' + '**, **'.join(maps) + '**', inline=False)
    await ctx.respond(embed=embed)

@mapsgroup.command(name='리셋')
async def resetmap(ctx: discord.ApplicationContext):
    maps = '스플릿/바인드/헤이븐/어센트/아이스박스/브리즈/프랙처/펄/로터스/선셋'.split('/')
    embed = discord.Embed(title='리셋 완료', color=0x00ffff, timestamp=datetime.datetime.now())
    await ctx.respond(embed=embed)

@mapsgroup.command(name='목록')
async def listmap(ctx: discord.ApplicationContext):
    embed = discord.Embed(title='맵 목록', description='**' + '**, **'.join(maps) + '**', color=0x00ffff, timestamp=datetime.datetime.now())
    await ctx.respond(embed=embed)

@bot.slash_command(name='팀원뽑기')
async def choiceTeam(ctx: discord.ApplicationContext, 팀원수: Option(int, "A팀의 팀원 수", required=False, default=0)):
    people = [i.id for i in ctx.author.voice.channel.members]
    number = 팀원수 or len(people) // 2
    a = []
    while len(a) < number:
        a.append(random.choice(people))
        del people[people.index(a[-1])]
    embed = discord.Embed(title='팀원 뽑기 결과', color=0x00ffff, timestamp=datetime.datetime.now())
    embed.add_field(name='A팀', value=', '.join(['<@' + str(i) + '>' for i in people]), inline=False)
    embed.add_field(name='B팀', value=', '.join(['<@' + str(i) + '>' for i in a]), inline=False)
    await ctx.respond(embed=embed)

@bot.slash_command(name='모드뽑기')
async def randommap(ctx: discord.ApplicationContext):
    embed = discord.Embed(title='모드 뽑기 결과', description='**' + random.choice('일반전/경쟁전/스파이크 돌격/신속플레이/데스매치/팀 데스매치/에스컬레이션'.split('/')) + '**', color=0x00ffff, timestamp=datetime.datetime.now())
    await ctx.respond(embed=embed)

class GunCategoryView(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
    @discord.ui.select(
        placeholder='총 종류',
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label='보조 무기',
                description='권총들+칼'
            ),
            discord.SelectOption(
                label='주 무기',
                description='권총 빼고 나머지+칼'
            ),
            discord.SelectOption(
                label='모두',
                description='모든 무기'
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if interaction.user.id != self.ctx.author: return
        mode = select.values[0]
        guns = ['칼']
        if mode == '보조 무기' or mode == '모두':
            guns.extend('클래식/쇼티/프렌지/고스트/셰리프'.split('/'))
        if mode == '주 무기' or mode == '모두':
            guns.extend('스팅어/스펙터/버키/저지/불독/가디언/팬텀/밴달/마샬/오퍼레이터/아레스/오딘'.split('/'))
        gun = random.choice(guns)
        embed = discord.Embed(title='총 뽑기 결과', description='**' + gun + '**', color=0x00ffff, timestamp=datetime.datetime.now())
        embed.set_image(url=gunimgs[gun])
        await interaction.response.send_message(embed=embed)
        
@bot.slash_command(name='총뽑기')
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
        self.add_item(discord.ui.InputText(label='Code', style=discord.InputTextStyle.long))
    def setctx(self, ctx):
        self.ctx = ctx
    async def callback(self, interaction: discord.Interaction):
        fn_name = "_eval_expr"
        env = {
            'bot': bot,
            'discord': discord,
            'ctx': self.ctx,
            '__import__': __import__
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
        
        await interaction.response.send_message('```\n' + str(await eval(f"{fn_name}()", env)) + '```', ephemeral=True)

@bot.slash_command(name='eval')
async def evalfn(ctx: discord.ApplicationContext):
    if ctx.author.id != bot.owner_id: return await ctx.respond('개발자 전용', ephemeral=True)
    modal = CodeModal(title='Code')
    modal.setctx(ctx)
    await ctx.send_modal(modal)

bot.run(open('token.txt').read())
