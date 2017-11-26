# WeatherTelop
天気のテロップ用の文字列を表示するものです

# 要求分析
天気予報を取得し、今日の天気明日の天気最高気温最低気温とできれば降水確率をテロップ用の文字列にする。

これはテロップで表示することを想定して作成する。

# 仕様
OnePleaceWether: APIを使用して一つの場所の天気情報を取得するクラス。文字列として返却できまた、辞書としても返却できる。

Wethers: 複数の場所の天気情報をまとめて保つためのクラス。テロップ用の文字列としてまとめて返却できる。

## 使用するもの

Apache License 2.0 が適用されたRequestsも使用します。

http://docs.python-requests.org/en/master/ Copyright (c)MMXVII. A Kenneth Reitz Project.

