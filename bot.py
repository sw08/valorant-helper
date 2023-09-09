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

bot.run("MTAyNzgwODA0MTY2OTc3NTM2Mg.GGuk9y.pOWXMMFg4LAtucj90rG2AogpZOyh7oHN8M-0VE")
