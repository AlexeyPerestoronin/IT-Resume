# Подготовка и запуск локального тестирования на Ubuntu-22.04
* Настройка OC:
    - `sudo apt update && sudo apt upgrade -y`
    - `sudo apt install -y ruby-full build-essential zlib1g-dev`
* Настройка переменных среды Ruby:
    - `echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc`
    - `echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc`
    - `echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc`
    - `source ~/.bashrc`
* Установка Bundler и Jekyll:
    - `gem install bundler jekyll`
* Запуск локального сервера для тестирования
    - `bundle install`
    - `bundle exec jekyll serve --livereload`
