import commandcript


@commandcript.script_task()
def prepare_os(ctx):
    """
    TODO: need provide some description
    """
    commandcript.ScriptExecutor(ctx.script_dir, False)\
        .add_cwd(commandcript.ENV_CONTEXT.PROJECT_GIT_DIR)\
        .add_commands([
            ['sudo apt update'],
            ['sudo apt install -y ruby-full build-essential zlib1g-dev'],
            ['sudo apt update'],
            ['bundle install'],
            ])\
        .execute(log="github-pages.prepare-os.log")


@commandcript.script_task()
def prepare_gem(ctx):
    """
    TODO: need provide some description
    """
    commandcript.ScriptExecutor(ctx.script_dir, ctx.launch)\
        .add_cwd(commandcript.ENV_CONTEXT.PROJECT_GIT_DIR)\
        .add_env({
            'GEM_HOME': '$HOME/gems',
            'PATH': '$HOME/gems/bin:$PATH',
        })\
        .add_commands([
            ['gem install bundler jekyll'],
            ['bundle install'],
            ])\
        .execute(log="github-pages.prepare-gem.log")


@commandcript.script_task()
def launch_local(ctx):
    """
    TODO: need provide some description
    """
    commandcript.ScriptExecutor(ctx.script_dir, ctx.launch)\
        .add_cwd(commandcript.ENV_CONTEXT.PROJECT_GIT_DIR)\
        .add_env({
                'GEM_HOME': '$HOME/gems',
                'PATH': '$HOME/gems/bin:$PATH',
            })\
        .add_command(["bundle exec jekyll serve"])\
        .execute(log="github-pages.launch-local.log")


collection = commandcript.invoke.Collection()
collection.add_task(prepare_os, name="prepare-os")
collection.add_task(prepare_gem, name="prepare-gem")
collection.add_task(launch_local, name="launch-local")
