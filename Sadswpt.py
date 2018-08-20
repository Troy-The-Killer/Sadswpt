#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

#  __  __           _       _
# |  \/  | ___   __| |_   _| | ___  ___
# | |\/| |/ _ \ / _` | | | | |/ _ \/ __|
# | |  | | (_) | (_| | |_| | | (_) \__ \
# |_|  |_|\___/ \__,_|\__,_|_|\___/|___/

import discord
import privado
from time import *
import asyncio
import datetime
import json
import requests
from random import *

# __     __         _                 _
# \ \   / /_ _ _ __(_) __ ___   _____(_)___
#  \ \ / / _` | '__| |/ _` \ \ / / _ \ / __|
#   \ V / (_| | |  | | (_| |\ V /  __/ \__ \
#    \_/ \__,_|_|  |_|\__,_| \_/ \___|_|___/

client = discord.Client()
token = privado.token()

#  ____
# / ___|___  _ __ ___  ___
#| |   / _ \| '__/ _ \/ __|
#| |__| (_) | | |  __/\__ \
# \____\___/|_|  \___||___/

preto = 0x000000
verde = 0x0BFF00
vermelho = 0xFF0000
Vermelho =0xFF0000
roxo = 0x4d0083
Magenta = 0xFF00FF

#__     __         _                 _
#\ \   / /_ _ _ __(_) __ ___   _____(_)___
# \ \ / / _` | '__| |/ _` \ \ / / _ \ / __|
#  \ V / (_| | |  | | (_| |\ V /  __/ \__ \
#   \_/ \__,_|_|  |_|\__,_| \_/ \___|_|___/

msg_id = None
msg_user = None

#   ___        _ _
#  / _ \ _ __ | (_)_ __   ___
# | | | | '_ \| | | '_ \ / _ \
# | |_| | | | | | | | | |  __/
#  \___/|_| |_|_|_|_| |_|\___|

@client.event
async def on_ready():
    print('-------------- Online --------------')
    print('Nome: {}'.format(client.user.name))
    print('  ID: {}'.format(client.user.id))
    print('------------------------------------')

    global user

    user = str(len(set(client.get_all_members())))

    await client.change_presence(game=discord.Game(name='💞 fb.com/sadsongswpt | {} Membros'.format(user),type=1,url='https://www.twitch.tv/soulindoefofo'),status='streaming')

@client.event
async def on_message(message):

    #    _     _           _
    #   / \   (_)_   _  __| | __ _
    #  / _ \  | | | | |/ _` |/ _` |
    # / ___ \ | | |_| | (_| | (_| |
    # /_/   \_\/ |\__,_|\__,_|\__,_|
    #       |__/

    if message.content.lower().startswith('s!ajuda'):
        ajuda = discord.Embed(
            title='📢 Meus Comandos',
            color=preto,
            description='**Moderação**\n'
                        '\n🔸 `s!avisos`\n'
                        '🔸 `s!clear`\n'
                        '🔸 `s!ban`\n'
                        '🔸 `s!votar`\n'
                        '🔸 `s!unmute`\n'
                        '🔸 `s!mute`\n'
                        '🔸 `s!statusbot`\n'
                        '\n**Livres**\n\n'
                        '🔹 `s!userinfo`\n'
                        '🔹 `s!convite`\n'
                        '🔹 `s!avatar`\n'
                        '🔹 `s!sadswpt`\n'
                        '🔹 `s!bitcoin`\n'
                        '🔹 `s!hora`\n'
                        '🔹 `s!botinfo`\n'
                        '\n**Joguinhos**\n\n'
                        '🔹 `s!idade`\n'
                        '🔹 `s!jokenpo`\n'
                        '🔹 `s!tabuada`\n'
                        '🔹 `s!dado`\n'
                        '🔹 `s!fibonacci`\n'
                        '🔹 `s!moeda`\n'
                        '🔹 `s!amor\n`'
                        '\n\n**Programação**\n\n'
                        '🔹 `s!py`\n'
                        '🔹 `s!js`\n'
                        '\n**Informações sobre os comandos:** `s!info`',
        )

        ajuda.set_thumbnail(url=client.user.avatar_url)
        return await client.send_message(message.channel, embed=ajuda)

    if message.content.lower().startswith('s!servidor'):

        user = message.author

        r1 = discord.Embed(
            title='Seja bem-vindo menino(a) triste!',
            color=Magenta,
            description="**•** O servidor está no intuito de conhecer um **novo público**, vocês podem conhecer diversas pessoas através de nossos **_canais de textos_**, mas claro, leia as regras antes de usufruir dos mesmos."
                        "\n\n"
                        "**•** Ei, espere! Nosso servidor disponibiliza um sistema de compras, após comprar o cargo <@&468980044966920193> você poderá escolher a cor que quiser para poder usufruir. Saiba mais acessando o #compra-de-cores.",
        )
        r2 = discord.Embed(
            title='Regras do Servidor',
            color=verde,
            description=":one: **Flood/Spam/Caps-lock excessivo**"
                        "\n\n"
                        "• Não envie mensagens similares, isso será considerado flood. Caso envie uma mensagem onde nela possuirá muitas letras idênticas isso será considerado spam (Ex.: Oieeeeeeee), enquanto ao Caps-lock excessivo nele será apenas considerado caso seja uma frase grande (Ex.: OI NORMIES, COMO VOCÊS ESTÃO?)."
                        "\n\n"
                        ":two: **Não ficar insistindo cargos**"
                        "\n\n"
                        "• Não peça, simplesmente não peça. Cada pedido que você faz querendo o cargo, menos chance você terá de receber o mesmo (Caso haja vagas na equipe iremos avisar no <#465121008282632192>)."
                        "\n\n"
                        ":three: **Uso de comandos em canais errados**"
                        "\n\n"
                        "• Caso queira usar um comando de algum Bot, use o <#465122014009491487>, caso queira ver seu rank, use o canal <#479439357543972864>."
                        "\n\n"
                        ":four: **Cargos especiais**"
                        "• Caso você se retire ou seja expulso do servidor, você não terá o direito aos seus antigos cargos especiais (Como os cargos de *cores*, *doador*, *doador VIP* e outros)."
                        "\n\n"
                        ":five: **Pornografia**"
                        "\n\n"
                        "• Conteúdo pornográfico em nosso servidor é proibido nos canais de conversas, caso queira enviar uma imagem/vídeo pornográfico, use o canal <#479815257490194442>."
                        "\n\n"
                        "• Conteúdo pornográfico é totalmente proibido no servidor. Caso seja pego enviando uma imagem/vídeo porn ou usando uma imagem porn de perfil e pedindo para outros usuários darem ?av, você será punido!"
                        "\n\n"
                        ":six: **Ofensa aos usuários**"
                        "\n\n"
                        "• Ofender algum membro do servidor é proibido. Seja respeitoso e interativo com o pessoal, lute por amigos mano!",
        )
        r3 = discord.Embed(
            title='Informações sobre o servidor',
            color=Magenta,
            description="• Categoria: `CHATKKK` » Está categoria é com o intuito de conversar com o pessoal, caso queira fazer amizades este é o lugar!"
                        "\n\n"
                        "• Categoria: `SORTEIOSKKK` »  Participe de nossos sorteios, venha receber premiações incríveis como coins em nosso Bot's ou até mesmo dinheiro real, fique mais ciente sobre a mesma analisando o <#465982211716546561>"
                        "\n\n"
                        "• Categoria: `INÍCIOKKK` » Área com canais importantes, lá serão anunciado coisas importantes ou irá registrar a entrada de novos membros. Fique atento lá! :D",
        )
        r4 = discord.Embed(
            title="Cargos da equipe",
            color=verde,
            description="• `Zap` » Eles são a auditoria do servidor! São os que comandam tudo, são os comandantes de tudo."
                        "\n\n"
                        "• `Adm` » Eles administram os Moderadores e Guardiões, dão funções ao mesmos para manter o servidor em uma forma confortável."
                        "\n\n"
                        "• `Moderador` » Como o nome diz, eles são a moderação do servidor, eles aplicam punições em pessoas más indesejadas, eles moderam os eventos que ocorrem no servidor durante a semana. Eles deixam o servidor agradável ao público."
                        "\n\n"
                        "• `Guardião` » Não possuem muitas permissões, eles apenas ajudam na interação com o público em geral do servidor. Mas mesmo assim fazem um ótimo trabalho!",
        )
        r5 = discord.Embed(
            title="Sistema de níveis",
            color=Magenta,
            description="Ao interagir com o pessoal, você receberá uma pequena quantia de Xp, entre **15 - 25**, de acordo com a sua quantia de Xp você possuirá um certo nível, na tabela abaixo irá mostrar os níveis necessários para cada cargo!"
        )
        r6 = discord.Embed(
            color=Magenta,
            description="\n"
        )

        r5.set_image(url="https://cdn.discordapp.com/attachments/465121342417534976/479461966243692565/unknown.png")
        r6.set_image(url="https://cdn.discordapp.com/attachments/465121342417534976/479462205746839553/Vhx75Kx.gif")

        await client.send_message(message.channel, 'Você vai receber às regras no privado!')

        await client.send_message(user, embed=r1)
        await client.send_message(user, embed=r2)
        await client.send_message(user, embed=r3)
        await client.send_message(user, embed=r4)
        await client.send_message(user, embed=r5)
        await client.send_message(user, embed=r6)

    #    _        _
    #   / \__   _(_)___  ___
    #  / _ \ \ / / / __|/ _ \
    # / ___ \ V /| \__ \ (_) |
    # /_/   \_\_/ |_|___/\___/


    if message.content.lower().startswith('s!aviso'):

        role = discord.utils.get(message.server.roles, name='Anúncios')

        if not role in message.author.roles:
            embed1 = discord.Embed(
                title='Ocorreu um Erro!',
                color=vermelho,
                description='`Sem Permissão:` Você precisa do cargo: `Anúncios`.'
            )
            embed1.set_footer(
                text=client.user.name,
                icon_url=client.user.avatar_url
            )
            return await client.send_message(message.channel, embed=embed1)

        msg = message.content.strip('s!aviso')

        embed2 = discord.Embed(
            title='Enviando Mensagem!',
            color=verde,
            description='`Mensagem :` **{}**'.format(msg)
        )

        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)

        x = list(message.server.members)
        s = 0

        for member in x:
            embed1 = discord.Embed(color=0x1ce1de, description=(msg))
            embed1.set_image(url="https://media.discordapp.net/attachments/471143059548012545/475514596778573834/FSj0ljq.gif")
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)

            try:
                await client.send_message(member, embed=embed1)
                print(member.name)
                s += 1

            except:
                pass

        print('\nAviso: Enviado para {} membros de {}'.format(s, len(x)))


        embed2 = discord.Embed(
            title='Mensagem Enviada!',
            color=verde,
            description="`SUCESSO:` \nMensagem enviada com sucesso para todos membros do servidor."
        )
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)

    #==================
    # Comandos → Clear:
    #==================

    if message.content.lower().startswith('s!clear'):
        if not message.author.server_permissions.administrator:
            erro = discord.Embed(
                title='Erro!',
                color=vermelho,
                description='Você não tem permisão!'
            )
            return await client.send_message(message.channel, embed=erro)

        limite = int(message.content.split().pop(1))
        await client.purge_from(message.channel, limit=limite)

        mensagem = discord.Embed(
            color=verde,
            description='{} Mensagens foram deletadas.'.format(limite)
        )

        purge = await client.send_message(message.channel, embed=mensagem)
        await asyncio.sleep(10)
        await client.delete_message(purge)

    #=====================
    # Comandos → UserInfo:
    #=====================

    if message.content.lower().startswith('s!userinfo'):
        try:
            user = message.author
            membro = message.mentions[0]
            embedinfo = discord.Embed(
                title='📝 Informações', color=0x83f68a,
                description='\n ')
            embedinfo.set_thumbnail(url=membro.avatar_url)
            embedinfo.add_field(name='🎓 | Usuário', value=membro.name)
            embedinfo.add_field(name='😂 | Apelido', value=membro.nick)
            embedinfo.add_field(name='🆔 | Id', value=membro.id)
            embedinfo.add_field(name='📆 | Desde de', value=membro.created_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='📆 | Entrou em', value=membro.joined_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='🎮 | Jogando', value=membro.game)
            embedinfo.add_field(name='💎 | Cargos',
                                value=len(([role.name for role in membro.roles if role.name != "@everyone"])))
            embedinfo.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedinfo)
        except:
            user = message.author
            embedinfo = discord.Embed(
                title='📝 Informações', color=0x83f68a,
                description='\n ')
            embedinfo.set_thumbnail(url=user.avatar_url)
            embedinfo.add_field(name='`🎓 | Usuário`', value=user.name)
            embedinfo.add_field(name='`😂 | Apelido`', value=user.nick)
            embedinfo.add_field(name='`🆔 | Id`', value=user.id)
            embedinfo.add_field(name='`📆 | Desde de`', value=user.created_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='`📆 | Entrou em`', value=user.joined_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='`🎮 | Jogando`', value=user.game)
            embedinfo.add_field(name='`💎 | Cargos`',
                                value=len(([role.name for role in user.roles if role.name != "@everyone"])))
            embedinfo.set_footer(
                text="Comando usado por {} às {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedinfo)

    #====================
    # Comandos → Convite:
    #====================

    if message.content.startswith("s!convite"):
        temp = await client.send_message(message.author, '📎 Convite criado: ' + message.content[8:] + '.')
        try:
            invite = await client.create_invite(message.channel, max_uses=2, temporary=True, xkcd=True)
            await client.edit_message(temp, '📎 Convite criado: ' + message.content[11:] + str(invite))

            aviso = discord.Embed(
                title='📎 Convite do Servidor',
                color=verde,
                description='Você receberá o convite no privado! 😉'
            )
            await client.send_message(message.channel, embed=aviso)

        except:
            await client.edit_message(temp, '😥 Falha ao criar convite.')

    #==================
    # Comandos → Votar:
    #==================

    if message.content.lower().startswith('s!votar'):
        try:
            msg = message.content[7:]
            embedvote = discord.Embed(
                title="🎭 VOTAÇÃO",
                color=0x1CF9FF,
                description=None
            )
            embedvote.set_thumbnail(url=message.author.avatar_url)
            embedvote.add_field(name='`Votação iniciada por:`', value=message.author.mention, inline=False)
            embedvote.add_field(name='`Titulo:`', value="{}".format(msg), inline=False)

            await client.send_typing(message.channel)
            gg = await client.send_message(message.channel, embed=embedvote)

            await client.add_reaction(gg, '✔')
            await client.add_reaction(gg, '❌')

        except discord.errors.HTTPException:
            await client.send_message(message.channel, "Insira um texto para iniciar a votação")

    #=================
    # Comandos → Info:
    #=================

    if message.content.lower().startswith('s!info'):
        try:
            recebe = message.content.strip('s!info')

            if int(recebe) == 1:
                sobre = discord.Embed(
                    title='Sobre: s!avisos',
                    color=verde,
                    description='Avisar sobre eventos/mudanças no servidor'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 2:
                sobre = discord.Embed(
                    title='Sobre: s!ban',
                    color=verde,
                    description='\n'
                                'Banir membros do servidor\n'
                                '\n**s!ban @membro**',
                )

                sobre.set_thumbnail(url="https://i.imgur.com/u69YiHx.png")
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 3:
                sobre = discord.Embed(
                    title='Sobre: s!votar',
                    color=verde,
                    description='Fazer votações para os membros'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 4:
                sobre = discord.Embed(
                    title='Sobre: s!unmute',
                    color=verde,
                    description='Desmultar o membro'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 5:
                sobre = discord.Embed(
                    title='Sobre: s!mute',
                    color=verde,
                    description='Mutar o membro'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 6:
                sobre = discord.Embed(
                    title='Sobre: s!statusbot',
                    color=verde,
                    description='Alterar o status do bot!'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 7:
                sobre = discord.Embed(
                    title='Sobre: s!userinfo',
                    color=verde,
                    description='Suas Informações / Informações do usuário'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 8:
                sobre = discord.Embed(
                    title='Sobre: s!convite',
                    color=verde,
                    description='Convite/Link do servidor'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 9:
                sobre = discord.Embed(
                    title='Sobre: s!avatar',
                    color=verde,
                    description='Ver o avatar dos membros / Ver seu avatar'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 10:
                sobre = discord.Embed(
                    title='Sobre: s!sadswpt',
                    color=verde,
                    description='Criadores e Participantes'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 11:
                sobre = discord.Embed(
                    title='Sobre: s!bitcoin',
                    color=verde,
                    description='Informações sobre o bitcoin'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 12:
                sobre = discord.Embed(
                    title='Sobre: s!hora',
                    color=verde,
                    description='Ver a hora'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 13:
                sobre = discord.Embed(
                    title='Sobre: s!botinfo',
                    color=verde,
                    description='Ver a hora'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 14:
                sobre = discord.Embed(
                    title='Sobre: s!idade',
                    color=verde,
                    description='Brincadeira da idade'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 15:
                sobre = discord.Embed(
                    title='Sobre: s!jokenpo',
                    color=verde,
                    description='Pedra, Papel e Tesoura'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 16:
                sobre = discord.Embed(
                    title='Sobre: s!tabuada',
                    color=verde,
                    description='Fazer tabuadas'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 17:
                sobre = discord.Embed(
                    title='Sobre: s!dado',
                    color=verde,
                    description='Joguinho do dado'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 18:
                sobre = discord.Embed(
                    title='Sobre: s!fibonacci',
                    color=verde,
                    description='Sequência de Fibonacci'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 19:
                sobre = discord.Embed(
                    title='Sobre: s!moeda',
                    color=verde,
                    description='Cara ou Coroa""'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 20:
                sobre = discord.Embed(
                    title='Sobre: s!amor',
                    color=verde,
                    description='Ship entre os membros!'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 21:
                sobre = discord.Embed(
                    title='Sobre: s!py',
                    color=verde,
                    description='Imprimir scripts em Python'
                )
                await client.send_message(message.channel, embed=sobre)

            if int(recebe) == 22:
                sobre = discord.Embed(
                    title='Sobre: s!js',
                    color=verde,
                    description='Imprimir scripts em JavaScript'
                )
                await client.send_message(message.channel, embed=sobre)

        except:
            lista = discord.Embed(
                color=preto,
                description='📋 Sobre os Comandos. **s!info <número>**\n'
                            '\n**Moderação**\n\n'
                            '\t🔸  `1` s!avisos\n'
                            '\t🔸  `2` s!ban\n'
                            '\t🔸  `3` s!votar\n'
                            '\t🔸  `4` s!unmute\n'
                            '\t🔸  `5` s!mute\n'
                            '\t🔸  `6` s!statusbot\n'
                            '\n**Livres**\n\n'
                            '\t🔹  `7` s!userinfo\n'
                            '\t🔹  `8` s!convite\n'
                            '\t🔹  `9` s!avatar\n'
                            '\t🔹 `10` s!sadswpt\n'
                            '\t🔹 `11` s!bitcoin\n'
                            '\t🔹 `12` s!hora\n'
                            '\t🔹 `13` s!botinfo\n'
                            '\n**Joguinhos**\n\n'
                            '\t🔹 `14` s!idade\n'
                            '\t🔹 `15` s!jokenpo\n'
                            '\t🔹 `16` s!tabuada\n'
                            '\t🔹 `17` s!dado\n'
                            '\t🔹 `18` s!fibonacci\n'
                            '\t🔹 `19` s!moeda\n'
                            '\t🔹 `20` s!amor\n'
                            '\n**Programação**\n\n'
                            '\t🔹 `21` s!py\n'
                            '\t🔹 `22` s!js\n',
            )
            lista.set_thumbnail(url="https://i.imgur.com/1qiJwa7.png")
            await client.send_message(message.channel, embed=lista)

    #====================
    # Comandos → Sadswpt:
    #====================

    if message.content.lower().startswith('s!sadswpt'):
        info = discord.Embed(
            color=preto,
            description='🔰 **Criador:**\n\n'
                        '\t• Troy\n'
                        '\n🌹 **Participantes**\n\n'
                        '\t• xiscronias\n'
                        '\t• Musashi\n'
                        '\t• bbto, o pescador\n'
                        '\t• ton\n'
                        '\n💞 **Informações:**\n\n'
                        '\t• {} Usuários\n\t• {} Servidores'.format(str(len(set(client.get_all_members()))),
                                                                            str(len(client.servers))
            )
        )
        info.set_thumbnail(url="https://i.imgur.com/oS8KRa5.gif")
        await client.send_message(message.channel, embed=info)

    #================
    # Comandos → Ban:
    #================

    if message.content.lower().startswith('s!ban'):
        if not message.author.server_permissions.ban_members:
            erro = discord.Embed(
                title='Erro!',
                color=vermelho,
                description='Você não tem permisão!'
            )
            await client.send_message(message.channel, embed=erro)

        else:
            try:
                membro = message.mentions[0]
                mensagem = discord.Embed(
                    title='Banido(a)!',
                    color=verde,
                    description='Usuário banido com sucesso!'
                )
                await client.send_message(message.channel, embed=mensagem)
                await client.ban(membro, delete_message_days=7)

            except:
                membro = message.author

                info = discord.Embed(
                    color=preto,
                    description='📝 **Como usar!**\n'
                                '\n\t`s!ban <@membro>`',
                )
                await client.send_message(message.channel, embed=info)

            finally:
                pass

    #=================
    # Comandos → Mute:
    #=================

    if message.content.lower().startswith('s!mute'):
        if not message.author.server_permissions.manage_roles:
            return await client.send_message(message.channel, 'Você precisa da permissão!')
        try:
            user = message.mentions[0]
            await client.send_message(message.channel, 'O usuário <@{}> foi mutado com sucesso do servidor.'.format(user.id))
            role = discord.utils.find(lambda r: r.name == 'Mutado', message.server.roles)
            await client.add_roles(user, role)
            await client.mute(membro)
        except:
            await client.send_message(message.channel, 'Você deve especificar um usuário!')
        finally:
            pass


    #===================
    # Comandos → Unmute:
    #===================

    if message.content.lower().startswith('s!unmute'):
        if not message.author.server_permissions.manage_roles:
            return await client.send_message(message.channel, 'Você precisa da permissão!')
        try:
            user = message.mentions[0]
            await client.send_message(message.channel, 'O usuário <@{}> foi desmultado com sucesso do servidor.'.format(user.id))
            role = discord.utils.find(lambda r: r.name == "Mutado", message.server.roles)
            await client.remove_roles(user, role)
        except:
            await client.send_message(message.channel, 'Você deve especificar um usuário!')
        finally:
            pass

    #=================
    # Comandos → Dado:
    #=================

    if message.content.startswith("s!dado"):
        choice = randint(1, 6)
        embeddad = discord.Embed(
            title='🎲 Dado',
            colour=0x1CF9FF,
            description='Joguei o dado, o resultado foi: {}'.format(choice)
        )
        await client.send_message(message.channel, embed=embeddad)

    #===================
    # Comandos → Avatar:
    #===================

    if message.content.lower().startswith('s!avatar'):
        try:
            membro = message.mentions[0]

            avatar1 = discord.Embed(
                title='Avatar',
                color=roxo,
                description='📷 [Download]('+membro.avatar_url+') {}'.format(membro.name)
            )

            avatar1.set_image(url=membro.avatar_url)
            await client.send_message(message.channel, embed=avatar1)

        except:
            membro = message.author

            avatar2 = discord.Embed(
                title='Seu avatar',
                color=roxo,
                description='📷 [Download]('+membro.avatar_url+') {}'.format(membro.name)
            )

            avatar2.set_image(url=membro.avatar_url)
            await client.send_message(message.channel, embed=avatar2)

    #==================
    # Comandos → Idade:
    #==================

    if message.content.lower().startswith("s!idade"):

        try:
            recebe = message.content.strip('s!idade')

            if int(recebe) >= 60:
                imprime = discord.Embed(
                    title='👴',
                    color=verde,
                    description='Idoso na área! 😂'
                )
                await client.send_message(message.channel, embed=imprime)

            elif int(recebe) >= 18:
                imprime = discord.Embed(
                    title='🍺',
                    color=verde,
                    description='Você é maior de idade!'
                )
                await client.send_message(message.channel, embed=imprime)

            elif int(recebe) <= 17:
                imprime = discord.Embed(
                    title='😥',
                    color=verde,
                    description='Você é menor de idade!'
                )
                await client.send_message(message.channel, embed=imprime)

            else:
                imprime = discord.Embed(
                    title='🍼',
                    color=verde,
                    description='Bebezinho! 😂'
                )
                await client.send_message(message.channel, embed=imprime)

        except:
            erro = discord.Embed(
                title='😡',
                color=vermelho,
                description='Você tem que informar a idade!'
            )
            await client.send_message(message.channel, embed=erro)

    #====================
    # Comandos → Jokenpo:
    #====================

    if message.content.lower().startswith('s!jokenpo'):
        try:
            recebe = message.content.strip('s!jokenpo')

            lista = ("Pedra", "Papel", "Tesoura")
            computador = randint(0,2)

            if computador == 0:
                if int(recebe) == 0:
                    opcao = discord.Embed(
                        color=verde,
                        description='Empate!'
                    )
                    await client.send_message(message.channel, embed=opcao)

                elif int(recebe) == 1:
                    opcao = discord.Embed(
                        color=vermelho,
                        description='Jogador Perdeu!'
                    )
                    await client.send_message(message.channel, embed=opcao)

                elif int(recebe) == 2:
                    opcao = discord.Embed(
                        color=verde,
                        description='Computador Venceu!'
                    )
                    await client.send_message(message.channel, embed=opcao)

                else:
                    opcao = discord.Embed(
                        color=vermelho,
                        description='Opção Inválida!'
                    )
                    await client.send_message(message.channel, embed=opcao)

            if computador == 1:
                if int(recebe) == 0:
                    opcao = discord.Embed(
                        color=vermelho,
                        description='Computador Perdeu!'
                    )
                    await client.send_message(message.channel, embed=opcao)
                elif int(recebe) == 1:
                    opcao = discord.Embed(
                        color=verde,
                        description='Empate!'
                    )
                    await client.send_message(message.channel, embed=opcao)
                elif int(recebe) == 2:
                    opcao = discord.Embed(
                        color=verde,
                        description='Jogador Venceu!'
                    )
                    await client.send_message(message.channel, embed=opcao)
                else:
                    opcao = discord.Embed(
                        color=vermelho,
                        description='Opção Inválida!'
                    )
                    await client.send_message(message.channel, embed=opcao)

            if computador == 2:
                if int(recebe) == 0:
                    opcao = discord.Embed(
                        color=verde,
                        description='Jogador Venceu!'
                    )
                    await client.send_message(message.channel, embed=opcao)
                elif int(recebe) == 1:
                    opcao = discord.Embed(
                        color=vermelho,
                        description='Computador Venceu!'
                    )
                    await client.send_message(message.channel, embed=opcao)
                elif int(recebe) == 2:
                    opcao = discord.Embed(
                        color=verde,
                        description='Empate!'
                    )
                    await client.send_message(message.channel, embed=opcao)
                else:
                    opcao = discord.Embed(
                        color=vermelho,
                        description='Opção Inválida!'
                    )
                    await client.send_message(message.channel, embed=opcao)

        except:
            tabela = discord.Embed(
                color=preto,
                description='🎮 Tabela. **s!jokenpo <número>**\n'
                            '\n\t`0` Pedra\n'
                            '\t`1` Papel\n'
                            '\t`2` Tesoura\n',
            )
            await client.send_message(message.channel, embed=tabela)

    #====================
    # Comandos → Tabuada:
    #====================

    if message.content.lower().startswith('s!tabuada'):
        try:
            valor = message.content.strip('s!tabuada')
            aux = 0

            tabuada = discord.Embed(
                title='🔢 Tabuada!',
                color=verde,
                description='`Tabuada de:` {}\n'.format(int(valor))
            )
            await client.send_message(message.channel, embed=tabuada)
            while(aux <= 10):
                await client.send_message(message.channel, '{0} X {1} = {2}'.format(aux, valor, (aux * int(valor))))
                aux = aux + 1
        except:
            tabela = discord.Embed(
                title='Tabuada!',
                color=preto,
                description='🔢 Tabela. **s!tabela <número>**\n'
            )
            await client.send_message(message.channel, embed=tabela)

    #======================
    # Comandos → Fibonacci:
    #======================

    if message.content.lower().startswith('s!fibonacci'):
        n = message.content.strip('s!fibonacci')

        info = discord.Embed(
            color=verde,
            description='Sequência de Fibonacci: {}'.format(n),
        )

        await client.send_message(message.channel, embed=info)

        t1 = 0
        t2 = 1

        await client.send_message(message.channel, '{}'.format(t1))
        await client.send_message(message.channel, '{}'.format(t2))

        cont = 3

        while(cont <= int(n)):
            t3 = t1 + t2
            await client.send_message(message.channel, '{}'.format(t3))
            t1 = t2
            t2 = t3
            cont += 1

        await client.send_message(message.channel, 'FIM')

    #====================
    # Comandos → Bitcoin:
    #====================

    elif message.content.lower().startswith('s!bitcoin'):
        await client.send_typing(message.channel)
        imgbtc = ('http://pngimg.com/uploads/bitcoin/bitcoin_PNG47.png')
        try:
            requeget = requests.get('http://api.promasters.net.br/cotacao/v1/valores?moedas=BTC&alt=json')
            btc = json.loads(requeget.text)
            nomebtc = (str(btc['valores']['BTC']['nome']))
            precobtc = (str(btc['valores']['BTC']['valor']))
            fontebtc = (str(btc['valores']['BTC']['fonte']))

            embedbtc = discord.Embed(color=0xffe100, )
            embedbtc.set_author(name='{}'.format(message.author.name),
                                icon_url=message.author.avatar_url)
            embedbtc.add_field(name='Nome:', value="{}".format(nomebtc))
            embedbtc.add_field(name='Valor:', value="{}".format(precobtc))
            embedbtc.add_field(name='Fonte:', value="{}".format(fontebtc))
            embedbtc.set_footer(text='Por: Troy')
            embedbtc.set_thumbnail(url=imgbtc)
            await client.send_message(message.channel, embed=embedbtc)
        except:
            await client.send_message(message.channel, 'ERROR!')

    #===================
    # Comandos → Python:
    #===================

    if message.content.lower().startswith('s!py'):
        usermsgcod = message.content[4:]
        await client.send_message(message.channel, '{} Enviou o seguinte código:\n```python\n{} \n```'.format(message.author.mention, usermsgcod))

    #=======================
    # Comandos → Javascript:
    #=======================

    if message.content.lower().startswith('s!js'):
        usermsgcod = message.content[4:]
        await client.send_message(message.channel, '{} Enviou o seguinte código:\n```javascript\n{} \n```'.format(message.author.mention, usermsgcod))

    #====================
    # Comandos → Relógio:
    #====================

    if message.content.lower().startswith("s!hora"):
        hora = discord.Embed(
            title='⌚ Relógio',
            color=verde,
            description='**{}**'.format(strftime('%H:%M:%S'))
        )
        await client.send_message(message.channel, embed=hora)

    #==================
    # Comandos → Moeda:
    #==================

    if message.content.startswith('s!moeda'):
        choice = randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '👑')
        if choice == 2:
            await client.add_reaction(message, '😃')

    #===================
    # Comandos → Status:
    #===================

    if message.content.startswith("s!statusbot"):
        gameName = message.content.replace("s!statusbot", "")
        if message.author.server_permissions.administrator:

            await client.change_presence(game=discord.Game(name=gameName))

            await client.send_message(message.channel, "`Status do bot foi alterado para: {}`".format(gameName))
        else:
            await client.send_message(message.channel, "⚠ Você precisa de permissão!")

    #====================
    # Comandos → BotInfo:
    #====================

    if message.content.lower().startswith('s!botinfo'):
        embedbot = discord.Embed(
            title='📢 Informações do Bot',
            color=0x83f68a,
            description='\n'
        )
        embedbot.set_thumbnail(url=client.user.avatar_url)
        embedbot.add_field(name='`💮 | Nome`', value=client.user.name, inline=True)
        embedbot.add_field(name='`🆔 | Id bot`', value=client.user.id, inline=True)
        embedbot.add_field(name='💠 | Criado em', value=client.user.created_at.strftime("%d %b %Y %H:%M"))
        embedbot.add_field(name='📛 | Tag', value=client.user)
        embedbot.add_field(name='‍💻 | Servidores', value=len(client.servers))
        embedbot.add_field(name='👥 | Usuarios', value=len(list(client.get_all_members())))
        embedbot.add_field(name='‍⚙️ | Programador', value="`Troy`")
        embedbot.set_footer(
            text="Comando usado por {} às {} Horas.".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)

        await client.send_message(message.channel, embed=embedbot)

    #=================
    # Comandos → Amor:
    #=================

    if message.content.lower().startswith('s!amor'):

        global medidor

        Numeros = randrange(0, 99)
        Membro = message.mentions[0]
        Autor = message.author

        if Numeros <= 15:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Vocês não combinam um com o outro.`\n'.format(Autor, Membro, Numeros),
            )

        elif Numeros <= 30:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Apenas amigos, porém, leais.`\n'.format(Autor, Membro, Numeros),
            )

        elif Numeros <= 50:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Da para formar um belo casal.`\n'.format(Autor, Membro, Numeros),
            )

        elif Numeros <= 75:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Vai dar namoro, Vai dar namoro...` 🎵\n'.format(Autor, Membro, Numeros),
            )

        elif Numeros <= 100:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Juntos até a morte!`\n'.format(Autor, Membro, Numeros),
            )

        medidor.set_thumbnail(url="https://i.imgur.com/zaEzzmY.gif")
        await client.send_message(message.channel, embed=medidor)

    #==================
    # Comandos → Cores:
    #==================

    if message.content.lower().startswith('s!cores'):
        adicionar = discord.Embed(
            title='💕 Adicionar a Cor',
            color=Magenta,
            description='s!cargo » `número`'
        )
        remover = discord.Embed(
            title='💕 Remover a Cor',
            color=Magenta,
            description='s!remover » `número`'
        )
        cores = discord.Embed(
            color=Magenta,
            description='💼 **Troca de Cores**'
                        '\n\n'
                        '🔹 `1` » <@&468980045222903818>\n'
                        '🔹 `2` » <@&468980045302464522>\n'
                        '🔹 `3` » <@&468980045159989260>\n'
                        '🔹 `4` » <@&469696089591906324>\n'
                        '🔹 `5` » <@&468980045159989278>\n'
                        '🔹 `6` » <@&469695871097896981>\n'
                        '🔹 `7` » <@&468980045080297473>\n'
                        '🔹 `8` » <@&470805545058697216>\n'
                        '🔹 `9` » <@&470805680329326612>',
        )
        await client.send_message(message.channel, embed=adicionar)
        await client.send_message(message.channel, embed=remover)

        reacao = await client.send_message(message.channel, embed=cores)

        await client.add_reaction(reacao, "⏩")

        global msg_id
        msg_id = reacao.id
        global msg_user
        msg_user = message.author

    #==================
    # Comandos → Cargo:
    #==================

    if message.content.lower().startswith('s!cargo'):

        role = discord.utils.get(message.server.roles, name='色')
        numero = message.content.strip('s!cargo')
        msg = message.author

        if not role in message.author.roles:
            erro = discord.Embed(
                title='😡 Erro!',
                color=vermelho,
                description='Você precisa do cargo: <@&468980044966920193>.'
            )
            await client.send_message(message.channel, embed=erro)
        else:
            if int(numero) == 1:
                role = discord.utils.find(lambda r: r.name == "Gelo", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045222903818>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 2:
                role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045302464522>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 3:
                role = discord.utils.find(lambda r: r.name == "Vinho", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045159989260>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 4:
                role = discord.utils.find(lambda r: r.name == "Roxo escuro", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&469696089591906324>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 5:
                role = discord.utils.find(lambda r: r.name == "Verde Água", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045159989278>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 6:
                role = discord.utils.find(lambda r: r.name == "Violeta", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&469695871097896981>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 7:
                role = discord.utils.find(lambda r: r.name == "Rosa Bebê", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045080297473>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 8:
                role = discord.utils.find(lambda r: r.name == "Carmesim", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&470805545058697216>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 9:
                role = discord.utils.find(lambda r: r.name == "Verde Claro", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&470805680329326612>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 10:
                role = discord.utils.find(lambda r: r.name == "Roxo", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&470805963876597760>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 11:
                role = discord.utils.find(lambda r: r.name == "Azul Real", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&471836427597119489>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 12:
                role = discord.utils.find(lambda r: r.name == "Limão", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&469696789839347722>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 13:
                role = discord.utils.find(lambda r: r.name == "Amêndoa", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045080297482>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 14:
                role = discord.utils.find(lambda r: r.name == "Khaki", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&471835648135921684>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 15:
                role = discord.utils.find(lambda r: r.name == "Amarelo", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&471836101925928970>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 16:
                role = discord.utils.find(lambda r: r.name == "Salmão", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045109657600>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 17:
                role = discord.utils.find(lambda r: r.name == "Azul Claro", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&470806392178081793>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 18:
                role = discord.utils.find(lambda r: r.name == "Vermelho escuro", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&471835250595725313>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 19:
                role = discord.utils.find(lambda r: r.name == "Preto", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045101268992>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 20:
                role = discord.utils.find(lambda r: r.name == "Marrom Pastel", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&472592332265357332>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 21:
                role = discord.utils.find(lambda r: r.name == "Azul", msg.server.roles)
                await client.add_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045072039957>. Adicionado com sucesso!',
                )
                await client.send_message(message.channel, embed=info)

            else:
                info = discord.Embed(
                    color=Vermelho,
                    description='💼 | Cargo: Não encontrado!',
                )
                await client.send_message(message.channel, embed=info)

    #====================
    # Comandos → Remover:
    #====================

    if message.content.lower().startswith('s!remover'):

        role = discord.utils.get(message.server.roles, name='色')
        numero = message.content.strip('s!remover')
        msg = message.author

        if not role in message.author.roles:
            erro = discord.Embed(
                title='😡 Erro!',
                color=Magenta,
                description='Você precisa do cargo: <@&468980044966920193>.'
            )
            await client.send_message(message.channel, embed=erro)
        else:
            if int(numero) == 1:
                role = discord.utils.find(lambda r: r.name == "Gelo", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045222903818>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 2:
                role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045302464522>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 3:
                role = discord.utils.find(lambda r: r.name == "Vinho", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045159989260>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 4:
                role = discord.utils.find(lambda r: r.name == "Roxo escuro", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&469696089591906324>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 5:
                role = discord.utils.find(lambda r: r.name == "Verde Água", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045159989278>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 6:
                role = discord.utils.find(lambda r: r.name == "Violeta", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&469695871097896981>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 7:
                role = discord.utils.find(lambda r: r.name == "Rosa Bebê", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045080297473>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 8:
                role = discord.utils.find(lambda r: r.name == "Carmesim", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&470805545058697216>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 9:
                role = discord.utils.find(lambda r: r.name == "Verde Claro", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&470805680329326612>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 10:
                role = discord.utils.find(lambda r: r.name == "Roxo", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&470805963876597760>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 11:
                role = discord.utils.find(lambda r: r.name == "Azul Real", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&471836427597119489>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 12:
                role = discord.utils.find(lambda r: r.name == "Limão", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&469696789839347722>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 13:
                role = discord.utils.find(lambda r: r.name == "Amêndoa", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045080297482>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)


            elif int(numero) == 14:
                role = discord.utils.find(lambda r: r.name == "Khaki", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&471835648135921684>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)


            elif int(numero) == 15:
                role = discord.utils.find(lambda r: r.name == "Amarelo", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&471836101925928970>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 16:
                role = discord.utils.find(lambda r: r.name == "Salmão", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045109657600>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 17:
                role = discord.utils.find(lambda r: r.name == "Azul Claro", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&470806392178081793>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 18:
                role = discord.utils.find(lambda r: r.name == "Vermelho escuro", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&471835250595725313>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 19:
                role = discord.utils.find(lambda r: r.name == "Preto", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045101268992>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 20:
                role = discord.utils.find(lambda r: r.name == "Marrom Pastel", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&472592332265357332>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            elif int(numero) == 21:
                role = discord.utils.find(lambda r: r.name == "Azul", msg.server.roles)
                await client.remove_roles(message.author, role)

                info = discord.Embed(
                    color=Magenta,
                    description='💼 | Cargo: <@&468980045072039957>. Removido com sucesso!'
                )
                await client.send_message(message.channel, embed=info)

            else:
                info = discord.Embed(
                    color=Vermelho,
                    description='💼 | Cargo: Não encontrado!'
                )
                await client.send_message(message.channel, embed=info)

    if message.content.lower().startswith('s!sorteio'):
        role = discord.utils.get(message.server.roles, name='Anúncios')
        canal = client.get_channel('465776229770067969')
        autor = message.author.mention

        if not role in message.author.roles:
            erro = discord.Embed(
                title='😡 Erro!',
                color=vermelho,
                description='Você precisa do cargo: <@&467810745598607360>. Para utilizar.'
            )
            await client.send_message(message.channel, embed=erro)

        else:
            await client.send_message(canal, '🎉 **SORTEIOS** 🎉'
                                             '\n\n'
                                             'Tem um sorteio relâmpago acontecendo. **Para participar basta reagir** 🎉'
                                             '\n\n'
                                             'Solicitem o cargo <@&465968428457656351> no <#465744338786189332> para está sempre por dentro de todos os sorteios.'
                                             '\n\n'
                                             'Você foi marcado por: %s. <:grrr:470022048257671190>'
                                             '\n\n'
                                             '**Boa sorte!**'
                                             '\n\n'
                                             'Tag: [ <@&465968428457656351> ]'%(autor),
            )
            await client.send_message(message.channel, 'Sucesso! Canal: <#465776229770067969>.')

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "⏩" and msg.id == msg_id and user == msg_user:
        cores = discord.Embed(
            color=Magenta,
            description='💼 **Troca de Cores**'
                        '\n\n'
                        '🔹 `10` <@&470805963876597760>\n'
                        '🔹 `11` <@&471836427597119489>\n'
                        '🔹 `12` <@&469696789839347722>\n'
                        '🔹 `13` <@&468980045080297482>\n'
                        '🔹 `14` <@&471835648135921684>\n'
                        '🔹 `15` <@&471836101925928970>\n'
                        '🔹 `16` <@&468980045109657600>\n'
                        '🔹 `17` <@&470806392178081793>\n'
                        '🔹 `18` <@&471835250595725313>\n'
                        '🔹 `19` <@&468980045101268992>\n'
                        '🔹 `20` <@&472592332265357332>\n'
                        '🔹 `21` <@&468980045072039957>',
        )
        reacao_2 = await client.edit_message(msg, embed=cores)
        await client.add_reaction(reacao_2, "⏪")

    if reaction.emoji == "⏪" and msg.id == msg_id and user == msg_user:
        cores = discord.Embed(
            color=Magenta,
            description='💼 **Troca de Cores**'
                        '\n\n'
                        '🔹 `1` » <@&468980045222903818>\n'
                        '🔹 `2` » <@&468980045302464522>\n'
                        '🔹 `3` » <@&468980045159989260>\n'
                        '🔹 `4` » <@&469696089591906324>\n'
                        '🔹 `5` » <@&468980045159989278>\n'
                        '🔹 `6` » <@&469695871097896981>\n'
                        '🔹 `7` » <@&468980045080297473>\n'
                        '🔹 `8` » <@&470805545058697216>\n'
                        '🔹 `9` » <@&470805680329326612>',
        )
        await client.edit_message(msg, embed=cores)

client.run(token)
