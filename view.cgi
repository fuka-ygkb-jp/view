#!/usr/local/bin/perl
$ver = "1.3";						#変更しないで下さい
#+------------------------------------------------------------------------
#|View(イラスト表示用補助プログラム - CGI方式)                  1999/ 8/ 8
#|(c)1999 不可思議絵の具(https://ygkb.jp/)
#|☆使い方
#| view.cgi?config&imagefile.jpg&imagefile.txt&作品名
#| －オプションの意味は以下の通り ( & で区切られています)－
#|   1番目:使用する設定ファイル名。
#|   2番目:表示するイメージファイル。
#|   3番目:そのイメージファイルの説明文。  (テキストのみ SJISで書くこと)
#|   4番目:作品の名前。                    (漢字でも良いがSJISで渡すこと)
#+------------------------------------------------------------------------
#●更新履歴
#1.3	Skin機能を実装 / 戻るボタンを付けた
#1.2	簡単なエラー処理とか付けた / GETからはパスを受け付けないようにした
#1.1	感想フォームの間違いを修正
#1.1β	感想フォームを付けてみる
#1.0	体裁を整える
#0.1	とりあえず作る
#+------------------------------------------------------------------------

### URLデコード
@d = split(/&/,$ENV{"QUERY_STRING"});

###設定保存ファイル呼出
require "./def/${d[0]}/${d[0]}.def";


### ドキュメントファイル読み込み
if ($d[2] ne "") {												#ファイル名が[指定されているなら]
	if (($d[2] =~ /.*\//) || ($d[1] =~ /.*\//)) {				#外部からの相対パス操作を許さない
		$d[3] = '外部からのパス指定は禁止されています';			#いたずらがあったら警告文
		$DoPutForm = 0;
		@data = (
			"\nハッキングはいけないことでつ(;´Д｀)",
			"すなおに えを かんしょうしようね☆　おにいさんとのやくそくだぞ☆　Σ(＞▽・)b\n",
			"それから、アニメをみるときは へやをあかるくして めを ちかづけないようにしましょうね.",
		);
	} else {
		open(DATA,"${dir_txt}$d[2]");							#読み込みモードでオープン
		chop(@data = <DATA>);									#改行コードを抜き取る
		close(DATA);											#ファイルをクローズ
		$Flag_NoDoc = 0;
	}
} else {														#[指定されていないなら]
	$Flag_NoDoc = 1;											#ゴミを取り除く(PerlのVerに因る？)
}

### 作品の名前が指定されていなかったらフラグを立てる
if ($d[3] eq "") { $Flag_NoName = 1; }


### HTML出力1
print <<"END";
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>

<!-- This page was created by View $ver  by Enogu Fukashigi (https://ygkb.jp/) -->
<!-- Imagefile name : $d[1]  /  Documentfile name : $d[2]  /  Title : $d[3] -->

<HEAD>
	<META http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
	<META http-equiv="Content-Style-Type" content="text/css">

END


### 名前が指定されていなかったら作品タイトルは表示しない
if ($Flag_NoName) { print "<TITLE>$title</TITLE>\n"; }
else              { print "<TITLE>$title / [ $d[3] ]</TITLE>\n"; }


print <<"END";

	<STYLE TYPE="text/css"><!--
		A{text-decoration:none;font-weight:bold}
	--></STYLE>
</HEAD>

<BODY $bg TEXT=$text LINK=$link ALINK=$alink VLINK=$vlink>
<BASEFONT SIZE=3>

END


### 名前が指定されていなかったら作品タイトルは表示しない
unless ($Flag_NoName) { print "<CENTER><FONT SIZE=+2><B>■$d[3]■</B></FONT></CENTER>\n\n<BR><HR><BR>\n\n"; }


### 絵を表示
if ($DoPutWaku) {				#枠を表示するなら
	if ($DoPutTable) {			#凝った枠を表示するなら

print <<"END";
	<CENTER><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 ALIGN=center>
		<TR>
			<TD $waku[0]><IMG SRC="./dummy.gif" WIDTH=$thick[1] HEIGHT=$thick[1]></TD>
			<TD $waku[1]><IMG SRC="./dummy.gif" WIDTH=$thick[1] HEIGHT=$thick[1]></TD>
			<TD $waku[2]><IMG SRC="./dummy.gif" WIDTH=$thick[1] HEIGHT=$thick[1]></TD>
		</TR>
		<TR>
			<TD $waku[3]><IMG SRC="./dummy.gif" WIDTH=$thick[1] HEIGHT=$thick[1]></TD>
			<TD><IMG SRC=\"${dir_img}$d[1]\" ALT=\"$d[3]\"></TD>
			<TD $waku[4]><IMG SRC="./dummy.gif" WIDTH=$thick[1] HEIGHT=$thick[1]></TD>
		</TR>
		<TR>
			<TD $waku[5]><IMG SRC="./dummy.gif" WIDTH=$thick[1] HEIGHT=$thick[1]></TD>
			<TD $waku[6]><IMG SRC="./dummy.gif" WIDTH=$thick[1] HEIGHT=$thick[1]></TD>
			<TD $waku[7]><IMG SRC="./dummy.gif" WIDTH=$thick[1] HEIGHT=$thick[1]></TD>
		</TR>
	</TABLE></CENTER>
	<BR>
END

	} else {					#普通のテーブルで良いなら
		print "<CENTER><TABLE BORDER=$thick[0]><TR><TD><IMG SRC=\"${dir_img}$d[1]\" ALT=\"$d[3]\"></TD></TR></TABLE></CENTER><BR>";
	}
} else {						#枠を表示しないなら
	print "<CENTER><IMG SRC=\"${dir_img}$d[1]\" ALT=\"$d[3]\"></CENTER><BR>";
}


### ドキュメントファイルが指定されているなら表示して良し
unless ($Flag_NoDoc) {
	print "<CENTER><TABLE BORDER=0><TR><TD $tblbg[0]><PRE>\n";


	### プレーンテキスト表示フィルタ
	foreach $line (@data) {
		$line =~ s/&/&amp;/g;
		$line =~ s/"/&quot;/g;
		$line =~ s/</&lt;/g;
		$line =~ s/>/&gt;/g;
		print $line."\n";
	}


	### HTML出力2
	print "</PRE></FONT></TD></TR></TABLE></CENTER>\n\n";
}


### フォームの表示が指定されているなら表示して良し
if ($DoPutForm) {
print <<"END";

<!-- 感想フォーム -->
<TABLE BORDER=0 CELLSPACING=2 CELLPADDING=6 ALIGN=center>
	<TR><TD ALIGN=center COLSPAN=2>
	<B><FONT COLOR=#6f55ff>
		<FONT SIZE=+2>■お暇でしたら感想をください(^^)■</FONT><BR>
		(Please send your impression!(^^))<BR><BR>
		ただし、現時点では新しめのブラウザでしか送れません。<BR>
		(But , you have to use IE4.0 NN3.0 later)
	</B></FONT>
	</TD></TR>

	<FORM ACTION=\"mailto:$addr\" METHOD=POST>

	<TR>
		<TD $tblbg[1]><B>お名前</B>(強制ではありません)<BR><B>NAME</B> (It's up to you whether you write this)</TD>
		<TD $tblbg[2]><INPUT TYPE=text NAME=name SIZE=40 MAXLENGS=60></TD>
	</TR>

	<TR>
		<TD $tblbg[1]><B>メールアドレス</B>(強制ではありません)<BR><B>E-MAIL Address</B> (It's up to you whether you write this)</TD>
		<TD $tblbg[2]><INPUT TYPE=text NAME=email SIZE=40 MAXLENGS=60></TD>
	</TR>

	<TR><TD COLSPAN=2 $tblbg[2]>
		<CENTER><TEXTAREA NAME=text ROWS=5 COLS=70 WRAP=hard>[about $d[1]]:</TEXTAREA></CENTER>
		<DIV ALIGN=center><INPUT TYPE=submit></DIV>
	</TD></TR>

	</FORM>

</TABLE>
END
}

print "\n<BR><BR><HR><BR>\n<CENTER><A HREF=\"$ENV{'HTTP_REFERER'}\"><FONT SIZE=+1>●戻る●</FONT></A></CENTER><BR>\n";
print "\n<HR>\n<DIV ALIGN=right><A HREF=\"https://ygkb.jp/\">View $ver by Enogu Fukashigi</A></DIV>\n</BODY></HTML>\n";

end;
