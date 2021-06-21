# atcoderの回答


## haskell環境

https://atcoder.jp/contests/abc199/rules
AtCoder環境に合わせてGHC 8.8.3をghcupで導入する

```
ghcup install 8.8.3
```

最新のcabalをinstall

```
ghcup install cabal latest
```

cabalでプロジェクト作成

```
cabal init
```

`cabal v2-build`
`cabal v2-exec`
ふたつをまとめたのが
`cabal v2-run`

`cabal v2-repl {source}`でソースファイルを読み込んでreplが起動する。
起動後`main`