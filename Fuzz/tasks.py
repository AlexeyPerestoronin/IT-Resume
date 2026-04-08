import commandcript

# Set up environment context
commandcript.ENV_CONTEXT\
    .add_env_var(env_var_name='COMMANDSCRIPT_SCRIPT_DIR', default_value='/home/alexey/MyLife/IT-Resume/Fuzz/.generated')\
    .add_env_var(env_var_name='PROJECT_GIT_DIR', default_value='/home/alexey/MyLife/IT-Resume')\
    .add_env_var(env_var_name='PROJECT_FUZZ_DIR', default_value='$PROJECT_GIT_DIR/Fuzz')


@commandcript.script_task()
def get_info(ctx):
    """
    Print to console information about active configuration of commandcript-tasks
    """
    width = max(max(len(key) for key in commandcript.ENV_CONTEXT.keys()), max(len(item) for item in commandcript.ENV_CONTEXT.values()))
    commandcript.INFO.log_line("Active environment configuration:")
    commandcript.INFO.log_line(f"|-{'-' * width}-|-{'-' * width}-|")
    for (key, value) in commandcript.ENV_CONTEXT.items():
        commandcript.INFO.log_line(f"| {key:<{width}} | {value:<{width}} |")


@commandcript.script_task()
def yapf(ctx):
    """
    Format python files in Fuzz
    """
    commandcript.ScriptExecutor(ctx.script_dir, ctx.launch)\
        .add_cwd(commandcript.ENV_CONTEXT.PROJECT_FUZZ_DIR)\
        .add_command([
                "yapf",
                "--style .style.yapf",
                "--verbose",
                "--recursive",
                "--in-place",
                "--parallel",
                f"--exclude '**.venv**'",
                f"{commandcript.ENV_CONTEXT.PROJECT_FUZZ_DIR}",
            ])\
        .execute(log="yapf.log")


namespace = commandcript.invoke.Collection()
namespace.add_task(get_info, name="get-info")
namespace.add_task(yapf, name="yapf")

import github_pages

namespace.add_collection(github_pages.collection, name='github-pages')
