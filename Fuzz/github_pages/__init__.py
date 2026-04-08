import commandcript


@commandcript.script_task()
def prepare_os(ctx):
    """
    Creates script for complex OS preparing for working with 'bundle'.
    Note: run manually with sudo access rights.
    """
    commandcript.ScriptExecutor(ctx.script_dir, False)\
        .add_cwd(commandcript.ENV_CONTEXT.PROJECT_GIT_DIR)\
        .add_commands([
            ['apt update'],
            ['apt install -y ruby-full build-essential zlib1g-dev'],
            ['apt update'],
            ['bundle install'],
            ])\
        .execute(log="github-pages.prepare-os.log")


@commandcript.script_task()
def prepare_gem(ctx):
    """
    Install 'bundle', 'jekyll' and install the site running environment for local testing.
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
def launch_local(ctx, kill: bool = False):
    """
    Launch local bundle-server for testing.
    """
    # TODO: need to implement kill 'bundle'-process optional ability
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
