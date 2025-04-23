from discord import app_commands
import discord.ext
import discord

class Tags(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=True)
    @app_commands.command(name="guildtag", description="Go read the damn faq.")
    async def guildtag(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            title="How to display the guild tag?",
            description="Follow the instructions in the video attached below to display the guild tag. For more information please refer to [This message](https://discord.com/channels/267735321695748096/1364073528978309130/1364074002590601337)",
            
        )
        embed.set_footer(text="Made with ♥ by Mero")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1206704887937630270/1364618545664753816/floorp_97C52eR63m.gif")

        
        await interaction.response.send_message(f"{member.mention}", embed=embed)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=True)
    @app_commands.command(name="gradientrole", description="Go read the damn faq.")
    async def gradientrole(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            title="Gradient roles",
            description="Gradient roles are currently only rolled out to a limit amount of servers, there is no way to speed the process up, for more information please refer to [This message](https://discord.com/channels/267735321695748096/1364073528978309130/1364074311098437692)",
            
            
        )
        embed.set_footer(text="Made with ♥ by Mero")
        
        await interaction.response.send_message(f"{member.mention}", embed=embed)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="botinfo", description="Info about the bot")
    async def botinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Bot info",
            description="This bot is made by Mero (mstrv) With the purpose of acting as a tag system for the https://discord.gg/pupy discord server.",
            
        )
        embed.set_footer(text="Made with ♥ by Mero")
        view = discord.ui.View()
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.url, label="Source code", url="https://github.com/hyfetch/ram-stick"))
        await interaction.response.send_message(embed=embed, view=view)




async def setup(bot):
    await bot.add_cog(Tags(bot))
