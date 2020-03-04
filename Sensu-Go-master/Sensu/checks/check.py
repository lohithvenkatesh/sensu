def CPU():
    return [
        'sensuctl asset create sensu-plugins-cpu-checks --url "https://assets.bonsai.sensu.io/68546e739d96fd695655b77b35b5aabfbabeb056/sensu-plugins-cpu-checks_4.0.0_debian_linux_amd64.tar.gz" --sha512 "da5a183ad1a1f76962561eed659c6184b3e5d6a412432e1ccb4297cce123c41f9a8bb4fdb9ab19663aada978ea862ab2bd5f00bc91e4769ddd87543f5662b3af"',
        'sensuctl asset create sensu-ruby-runtime --url "https://assets.bonsai.sensu.io/5123017d3dadf2067fa90fc28275b92e9b586885/sensu-ruby-runtime_0.0.10_ruby-2.4.4_debian_linux_amd64.tar.gz" --sha512 "a28952fd93fc63db1f8988c7bc40b0ad815eb9f35ef7317d6caf5d77ecfbfd824a9db54184400aa0c81c29b34cb48c7e8c6e3f17891aaf84cafa3c134266a61a"',
        'sensuctl asset list', "sensuctl check create check-cpu \
               --command 'check-cpu.rb -w 75 -c 90' \
               --interval 60 \
               --subscriptions system \
               --runtime-assets sensu-plugins-cpu-checks,sensu-ruby-runtime"]


def DISK():
    return [
        'sensuctl asset create sensu-plugins-disk-checks --url "https://assets.bonsai.sensu.io/73a6f8b6f56672630d83ec21676f9a6251094475/sensu-plugins-disk-checks_5.0.0_debian_linux_amd64.tar.gz" --sha512 "efcc00a70ed8ebcab401b7dbd595d770a2b441e56d99143a923cbfc98977f6d085388b7411da706d47e6150b31ffa9b41ba78a0ee35a0e19eb21eee713009e19"',
        "sensuctl check create check-disk \
          --command 'check-disk-usage.rb -w 75 -c 90 -p /snap' \
          --interval 60 \
          --subscriptions system \
          --runtime-assets sensu-plugins-disk-checks,sensu-ruby-runtime"]


def Load():
    return ['sensuctl asset create sensu-plugins-load-checks --url "https://assets.bonsai.sensu.io/1accacdd780175a02183e722effa0986e6472f21/sensu-plugins-load-checks_5.0.0_debian_linux_amd64.tar.gz" --sha512 "3e171c28e6bdaecc7d164fa4c49dea193e95508609436866bc973b14ce49a0d07ce5314a78010490f954790d9194260cc59344e2a0c0fec74ae856973674dd66"',
       "sensuctl check create check-load \
        --command 'check-load.rb -c 2,200,200 -w 1,100,100' \
        --interval 60 \
        --subscriptions system \
        --runtime-assets sensu-plugins-load-checks,sensu-ruby-runtime"]


def Memory():
    return ['sensuctl asset create sensu-plugins-memory-checks --url "https://assets.bonsai.sensu.io/c5391d4ae186484226732344b35cf95c0b07b8ec/sensu-plugins-memory-checks_4.0.0_debian_linux_amd64.tar.gz" --sha512 "3c61ab6f4eb5dea4ee816e4f9a4f857660ac32648d0ecd7804e1827351d8fe021f29e557d9600ecac8cd16d261c8ff2dc113790a544ce1148a8cb321546552d6"',
       "sensuctl check create check-memory \
        --command 'check-memory-percent.rb -w 70 -c 80' \
        --interval 60 \
        --subscriptions system \
        --runtime-assets sensu-plugins-memory-checks,sensu-ruby-runtime"]


def Swap():
    return ['sensuctl asset create sensu-plugins-memory-checks --url "https://assets.bonsai.sensu.io/c5391d4ae186484226732344b35cf95c0b07b8ec/sensu-plugins-memory-checks_4.0.0_debian_linux_amd64.tar.gz" --sha512 "3c61ab6f4eb5dea4ee816e4f9a4f857660ac32648d0ecd7804e1827351d8fe021f29e557d9600ecac8cd16d261c8ff2dc113790a544ce1148a8cb321546552d6"',
       "sensuctl check create check-swap \
--command 'check-swap-percent.rb -w 70 -c 80' \
--interval 60 \
--subscriptions system \
--runtime-assets sensu-plugins-memory-checks,sensu-ruby-runtime"]
