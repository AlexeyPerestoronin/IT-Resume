# Обновление системы
sudo apt update && sudo apt upgrade -y

# Установка Ruby, Bundler и зависимостей
sudo apt install -y ruby-full build-essential zlib1g-dev

# Настройка переменных среды Ruby (важно!)
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Установка Bundler и Jekyll
gem install bundler jekyll

# Запуск
bundle install
bundle exec jekyll serve --livereload