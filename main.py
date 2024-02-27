import discord
import decouple
from discord.ext import commands
from discord.ext import tasks

Mangalassery_Neelakandan=commands.Bot(command_prefix='/',intents=discord.Intents.all())

@Mangalassery_Neelakandan.event
async def on_ready():
    print("Bot is running")
    await Mangalassery_Neelakandan.tree.sync()

@Mangalassery_Neelakandan.event
async def on_member_join(member):
    message=f"welcome the server {member.name}"
    welcome_channel=Mangalassery_Neelakandan.get_channel(1210208087403925585)
    await welcome_channel.send(message)
    await member.send(message)

class Mymodal(discord.ui.Modal):
    def __init__(self, title: str):
        super().__init__(title=title)
        self.add_item(discord.ui.TextInput(label="Your response", placeholder="Enter your response"))
        self.submitted = False  # Initialize submitted flag to False

    
    async def on_submit(self, interaction: discord.interactions):
        if self.submitted:
            return  # Prevent duplicate responses

        role_name = "moderator"  # Replace with the actual role name
        role = discord.utils.get(interaction.guild.roles, name=role_name)
        member_name = interaction.user.name
        response = self.children[0].value
        await interaction.response.send_message("Your response has been submitted.", ephemeral=True)
     
        async def send_to_moderators():
            if interaction.guild:
                for member in interaction.guild.members:
                    await role.send(f"A support ticket has been submitted by {member_name}. Response: {response}")
        
        discord.app_commands.guild_only(interaction).loop.create_task(send_to_moderators())
        
@Mangalassery_Neelakandan.tree.command(name="support-ticket")
async def support(interation):
    my_modal=Mymodal(title="Tell me, What's your problem")
    await interation.response.send_modal(my_modal)













Mangalassery_Neelakandan.run(decouple.config("TOKEN"))
