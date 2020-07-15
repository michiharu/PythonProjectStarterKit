# Python Project Starter Kit

Pythonコードをプロジェクトとしてメンテナンスするための構成を考えたリポジトリです。

前提環境は次の通りです。

* Python3.8をインストール済み
* pipenvをインストール済み
* VSCodeをエディターとして使用

導入方法は次の通りです。

まずはクローンして、新しいリポジトリを設定します。
```
git clone https://github.com/michiharu/PythonProjectStarterKit.git
mv PythonProjectStarterKit [新しいプロジェクト名]
cd [新しいプロジェクト名]
git remote remove origin
git remote add origin [新しいリモートリポジトリのURL]
```

次にvscodeの設定をします。以下はmacの例です。
windowsの場合は`"python.pythonPath"`に、`".venv\\Scripts\\python.exe"`を設定します。
`.vscode/settings.json`は、チームメンバーでマシンのOSが統一されているならリポジトリに含めた方が楽でしょう。

```
mkdir .vscode
touch .vscode/settings.json
cat << EOS > .vscode/settings.json
{
  "python.venvPath": ".venv",
  "python.pythonPath": ".venv/bin/python",
  "python.envFile": "${workspaceFolder}/.env",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "python.formatting.provider": "black",
  "python.linting.flake8Args": [
    "--max-line-length=88",
    "--ignore=W503,E203,E722"
  ]
}
EOS
```

最後に動作確認です。VSCodeで`.py`ファイルを開いて、関数のdocstringsなど表示されることを確認してください。

```
pipenv install --dev --pre
pipenv run test
```