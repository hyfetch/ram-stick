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
            title="Gradient roles"
            
        )
        embed.set_footer(text="Made with ♥ by Mero")
        embed.add_field(name="Where do I get gradient roles within the server?", value="You can set a gradient-colored role for yourself in <id:customize>")
        embed.add_field(name="How do I get them in my server?", value="Gradient colored roles are currently part of an experiment and the roll-out is limited. There is no way to speed the process up and the only way currently is to wait.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1168573744214724629/1365021147732774922/gradient.gif")
        await interaction.response.send_message(f"{member.mention}", embed=embed)




    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="botinfo", description="Info about the bot")
    async def botinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Bot info",
            description="This bot is made by <@852891241125117962> With the purpose of acting as a tag system for the https://discord.gg/pupy discord server.",
            
        )
        embed.set_footer(text="Made with ♥ by Mero")
        view = discord.ui.View()
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.url, label="Source code", url="https://github.com/hyfetch/ram-stick"))
        await interaction.response.send_message(embed=embed, view=view)
    


    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=True)
    @app_commands.command(name="english", description="People don't read rules!!!")
    async def english(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            title="This server is english only!!",
            description="As the moderators cannot moderate in all languages the decision has been made to keep the server only to the english language."
        )
        embed.set_footer(text="Made with ♥ by Mero")
        await interaction.response.send_message(f"{member.mention}", embed=embed)





async def setup(bot):
    await bot.add_cog(Tags(bot))
