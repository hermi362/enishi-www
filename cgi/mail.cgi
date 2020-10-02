#!/usr/local/bin/perl --

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\  Creation company : DIC Inc.
#\\  http://www.d-ic.com/
#\\  DIC-Studio. Mail_v2s Version:1.82 (2012/09/07)
#\\  Copyright (C) DIC All Rights Reserved. このスクリプトの再配布などを禁止します.
#\\  バグ報告は studio@d-ic.com 宛にお願いします。
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

##*****<< 設置方法 >>******************************************************************************
##
## ※ＣＧＩファイルの初期設定をお使いの環境に合わせてカスタマイズしてください。
## ※お使いのサーバによっては下のファイル構成では動作しない場合があります。
##   その際はサーバ管理者にお問い合わせください。
## ※"[]"内の数字はパーミッションです。
## ※"form.html"は、同梱の"sample.html"を参考に作成してください。
##
## public_html/
##  |         form.html
##  |
##  +-- cgi-bin/
##       |
##       +-- mail_v2s/
##                  mail.cgi	[755]
##                  jcode.pl
##                  stdio.pl
##                  check.html
##                  thanks.html
##                  title.gif
##                  remail.txt
##
##*****<< バージョンアップ情報 >>******************************************************************
##
## 2012/09/07 .....Ver1.82
##   ・自動返信メールの件名を自由に設定できるように改良。
##   ・件名に入力値を差し込む機能を追加。
##
## 2007/05/09 .....Ver1.8
##   ・セキュリティ対策
##
## 2007/05/08 .....Ver1.7
##   ・送信メールアドレス、メール件名、必須項目、送信完了ページのURL、をmail.cgiにて設定するように修正。
##
## 2004/12/05 .....Ver1.6
##   ・同じname属性が複数あった場合に重複してしまうバグを修正。
##
## 2003/07/11 .....Ver1.5
##   ・入力フォームにてEmailを省略した場合エラーを起こすバグを修正。
##
## 2003/06/02 .....Ver1.40
##   ・フォームのページで 必須項目、送信完了ページ、送信先、件名 を指定できるように修正。
##   ・送信完了時に任意のページへジャンプできるように機能追加。（テンプレートとして読み込むのではなく、ジャンプするように修正）
##   ・テンプレートＨＴＭＬなどの細かい修正
##
## 2002/12/11 .....Ver1.30
##   ・送信後にホームページに戻れるようにリンクを貼る機能を追加
##   ・テンプレートＨＴＭＬなどの細かい修正
##
## 2002/10/03 .....Ver1.20
##   ・テンプレートＨＴＭＬなどの細かい修正
##
##*************************************************************************************************


##=====================================
##           初期設定部分             =
##=====================================

# 送信メールアドレス
$mailaddress = 'enishi.office@gmail.com';


# 件名
# ↓のように、「_%name値%_」を挿入することで、入力情報を差し込むことができます。
# $subject = '[_%お名前%_さま]HPから問合せ';

# 管理者宛	'[_%name%_さま]HPから問合せ';
$subject = 'HPから問合せ';

# ユーザ宛
$re_subject = 'お問合せありがとうございます';


# 入力必須項目
@necessary = ('name','kana','zip1','zip2','add','tel','email','email_confirm','approval');

# 送信完了画面のURL
$thank_page = '';

# sendmailのパス
$sendmail = '/usr/sbin/sendmail';

# テンプレート（自動返信メールの本文）
#$remail_txt = './remail.txt';

# テンプレートＨＴＭＬ（入力確認用）
$template1 = './check.html';

# 確認画面のテーブルデザイン
$tablewidth = '650';		# テーブルの横幅
$bgcolor1 = '#FFFFFF';		# 項目の色
$bgcolor2 = '#FFFFFF';		# 内容の色
$border = '0';				# 枠線の太さ（なし=0）
$bordercolor = '#999999';	# 枠線の色
$cellpadding = '0';			# cellpadding



##=====================================
## サブルーチン                       =
##=====================================
require './jcode.pl';
require './stdio.pl';



#□□□□□□□□□□□□ ここから下を修正した場合にはサポート対象外になります。ご注意ください。 □□□□□□□□□□□

##=====================================
## データを受け取る                   =
##=====================================
%param = ();
@key_list = stdio::getFormData(\%param,0,sjis,1," \/ ",);





#□□□□□□□□□□□□□□□□□□□ モード指定 "なし" □□□□□□□□□□□□□□□□□□□□□□□
if(!$param{'mode'}){


if($param{'email'} ne $param{'email_confirm'}) {
	&error('入力エラー',"メールアドレスが一致しません<BR><BR>$param{'email'}<BR>$param{'email_confirm'}");
}

##=====================================
## 必須項目の入力チェック             =
##=====================================
foreach(@necessary){

	if(!$param{$_}){
		if($_ eq 'name') {
			$hissu_check .= "・お名前<br>";
		} elsif($_ eq 'kana') {
			$hissu_check .= "・フリガナ<br>";
		} elsif($_ eq 'zip1') {
			$hissu_check .= "・郵便番号(前)<br>";
		} elsif($_ eq 'zip2') {
			$hissu_check .= "・郵便番号(後)<br>";
		} elsif($_ eq 'add') {
			$hissu_check .= "・ご住所<br>";
		} elsif($_ eq 'tel') {
			$hissu_check .= "・電話番号<br>";
		} elsif($_ eq 'email') {
			$hissu_check .= "・メールアドレス<br>";
		} elsif($_ eq 'email_confirm') {
			$hissu_check .= "・メールアドレス(確認用)<br>";
		} elsif($_ eq 'approval') {
			$template1 = './check_approval.html';
			#&error_not_approval('入力エラー', "「個人情報の取り扱いについて」の同意するチェックボックスにチェックサインがされていません、メッセージやお問い合わせ内容は送信されますが返答に関してはチェックサインをされた方のみとさせて頂く事を何卒ご了承下さい。<BR><BR>※入力した内容を確認してください、上記内容にてよろしければ 送信ボタン をクリックしてください。<BR>");
		}
	}
}

if($hissu_check){ &error('入力エラー',"以下の必須項目に入力がありませんでした。<br><br>$hissu_check"); }


##=====================================
## Eメール入力のチェック              =
##=====================================
if($param{'email'}){
	if($param{'email'} =~ /^\S+@\S+\.\S+/){ ; }
	else{ &error('入力エラー',"Eメールアドレスの入力を間違えています。"); }
	if($param{'email'} =~ /Ａ|Ｂ|Ｃ|Ｄ|Ｅ|Ｆ|Ｇ|Ｈ|Ｉ|Ｊ|Ｋ|Ｌ|Ｍ|Ｎ|Ｏ|Ｐ|Ｑ|Ｒ|Ｓ|Ｔ|Ｕ|Ｖ|Ｗ|Ｘ|Ｙ|Ｚ/){ &error('入力エラー',"Eメールアドレスの入力が間違えています。半角英数字を使用してください。"); }
	if($param{'email'} =~ /ａ|ｂ|ｃ|ｄ|ｅ|ｆ|ｇ|ｈ|ｉ|ｊ|ｋ|ｌ|ｍ|ｎ|ｏ|ｐ|ｑ|ｒ|ｓ|ｔ|ｕ|ｖ|ｗ|ｘ|ｙ|ｚ/){ &error('入力エラー',"Eメールアドレスの入力が間違えています。半角英数字を使用してください。"); }
	if($param{'email'} =~ /[^\-\.\@\_0-9a-zA-Z]/){ &error('エラー','入力を間違えています。'); }
}


##=====================================
## 特殊記号を変換する                 =
##=====================================
foreach (@key_list) {
	$param{$_} =~ s/&/＆/g;
	$param{$_} =~ s/\"/”/g;
	$param{$_} =~ s/</＜/g;
	$param{$_} =~ s/>/＞/g;
	$param{$_} =~ s/,/，/g;
	$param{$_} =~ s/\'/’/g;
	$param{$_} =~ s/\n/ /g;
}


##=====================================
## 入力確認画面の一部                 =
##=====================================
@key_list = grep(!$seen{$_}++, @key_list);

foreach(@key_list){

	&jcode::convert(\$param{\$_},'Shift_JIS');

	if($_ eq 'submit'){ next; }
	
	if($_ eq 'name'){
		$title_name = 'お名前';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"お名前\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'kana') {
		$title_name = 'フリガナ';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"フリガナ\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'zip1') {
		$title_name = '郵便番号';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}-$param{'zip2'}<input type=\"hidden\" name=\"郵便番号\" value=\"$param{$_}-$param{zip2}\"></td></tr>";
	} elsif($_ eq 'add') {
		$title_name = 'ご住所';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"ご住所\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'tel') {
		$title_name = '電話番号';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"電話番号\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'email') {
		$title_name = 'メールアドレス';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"メールアドレス\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'hope') {
		$title_name = '希望の連絡手段';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"希望の連絡手段\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'msg') {
		$title_name = 'お問合せ内容';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"お問合せ内容\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'type') {
		$title_name = '緑化の種類';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"緑化の種類\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'place') {
		$title_name = '緑化予定場所';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"緑化予定場所\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'question') {
		$title_name = '質問・要望等';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"質問・要望等\" value=\"$param{$_}\"></td></tr>";
	}

	#if($param{$_}){ $param = $param{$_}; }
}


$mail = qq|
<input type="hidden" name="mode" value="mailsend">


   $mail_table

|;


##=====================================
## 確認テンプレートファイルをオープン =
##=====================================
if(!open(HTML,$template1)){ &error('システムエラー',"テンプレートファイル ( $template1 ) がオープンできません。");}
@html = <HTML>;
close(HTML);


##=====================================
## 特殊文字を置き換え                 =
##=====================================
$dic = qq|<div align="right" class="copyright">- <a href="http://www.d-ic.com/" target="_top">メール送信プログラム： DIC-Studio</a> -</div>|;
foreach(@html){
	if($_ =~ /_%copyright%_/){ $flag = '1'; }
	s/_%mail%_/$mail/g;
	s/_%Email%_/$mailaddress/g;
	s/_%copyright%_/$dic/g;
}
if(!$flag){ &error('システムエラー',''); }


##=====================================
## 確認画面表示                       =
##=====================================
print <<"EOF";
Content-type: text/html

@html
EOF
exit;
}	# モード指定 なし ここまで


#□□□□□□□□□□□□□□□□□□□ モード指定 "mailsend" □□□□□□□□□□□□□□□□□□□□□□□
if($param{'mode'} eq 'mailsend'){

##=====================================
## 特殊記号を変換する                 =
##=====================================
foreach (@key_list) {
	$param{$_} =~ s/\n/ /g;
	$param{$_} =~ s/&/＆/g;
	$param{$_} =~ s/\"/”/g;
	$param{$_} =~ s/</＜/g;
	$param{$_} =~ s/>/＞/g;
	$param{$_} =~ s/,/，/g;
	$param{$_} =~ s/\'/’/g;
	
	$subst{$_} = $param{$_};
}


##=====================================
## メール件名
##=====================================
@subject = ($subject);
@re_subject = ($re_subject);

$subject = &dicTag(@subject);
$re_subject = &dicTag($re_subject);


##=====================================
## メール本文                         =
##=====================================
$mailbody = "$subject\n\n";

foreach(@key_list){
	if($_ eq 'mode'){ next; }
#	elsif($_ eq 'remail'){ next;}
	
	$mailbody .= "■$_\n$param{$_}\n\n";
#	$remailbody .= "\n■$_\n$param{$_}\n";
}


##=====================================
## メール送信                         =
##=====================================
if($param{'email'}){ $mailfrom = $param{'email'}; }
else{ $mailfrom = 'xxxxx@xxxx.xxx'; }

%header = (
    'To'      => $mailaddress,
    'From'    => $mailfrom,
    'Subject' => $subject
);
$result = stdio::sendmail($sendmail, \%header,$mailbody, 0, 0,);
if(!$result){ &error('システムエラー',"メールの送信に失敗しました。"); }

##=====================================
## メール送信完了表示                 =
##=====================================
=for comment
print <<"EOF";
Content-type: text/plain

To      => $mailaddress
From    => $mailfrom
Subject => $subject
$mailbody

To      => $mailfrom
From    => $mailaddress
Subject => $re_subject
$re_mailbody
EOF
exit;
=cut


if($thank_page){
	print "Location: $thank_page\n\n";
}else{
	print <<"EOF";
Content-type: text/html

<html>
<head>
<title>メールフォーム</title>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<style type="text/css">
a {
    color: #000;
    text-decoration: none;
}
a:hover { color: #990000; }
body { font-size: 12px; }
h2 { text-align: center; }
div {
    margin:0 auto;
    text-align: right;
    width: 600px;
}
</style>
</head>

<body>
<div>
    <h2>送信完了</h2>
    <br><br><br><br><br><br>
</div>
</body>
</html>
EOF
exit;
}
}	# モード指定 mailsend ここまで


##=====================================
## エラー表示                         =
##=====================================
sub error {
print <<"END";
Content-type: text/html

<html><head><title>!ERROR!</title>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<style type="text/css">

/* 背景設定 */
body#submit_error {
	background-image: url(http://fujiokafix.atumari.net/template/bg2.jpg);
	background-size: cover;
	background-position: 50% 0;
	height: 100%;
}
/* リンク */
#submit_error a {
  color: #000;
  text-decoration: none;
}
#submit_error a:hover {
	color: #33A400;
}
/* エラー項目表示テーブル設定 */
#submit_error table {
  width: 660px;
  border-width: 0px;
	margin-top: 50px;
}
#submit_error td { 
	font-size: 14px;
}
/* 「入力エラー」表示td */
#submit_error #error_title {
	font-size: 25px;
	font-weight: bold;
	color: #f00;
}

</style>
</head>
<body id="submit_error">
<div id="top"></div>
<table align="center">
 <tr>
  <td id="error_title"><b>$_[0]</b></td>
 </tr>
 <tr>
  <td>
   <br>
    <b>$_[1]</b>
    <BR>
    <p><a href="JavaScript:history.back()">こちらをクリックして前の画面に移動してください。</a>
  </td>
 </tr>
</table>
<script type="text/javascript" language="javascript">
window.parent.scrollTo("0","200");
</script>
</body></html>
END
exit;
}

#-- 同意チェックがされてなかった場合 --#
sub error_not_approval {
print <<"END";
Content-type: text/html

<html><head><title>!ERROR!</title>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<style type="text/css">

/* 背景設定 */
body#submit_error {
	background-image: url(http://fujiokafix.atumari.net/template/bg2.jpg);
	background-size: cover;
	background-position: 50% 0;
	height: 100%;
}
/* リンク */
#submit_error a {
  color: #000;
  text-decoration: none;
}
#submit_error a:hover {
	color: #33A400;
}
/* エラー項目表示テーブル設定 */
#submit_error table {
  width: 660px;
  border-width: 0px;
	margin-top: 50px;
}
#submit_error td { 
	font-size: 14px;
}
/* 「入力エラー」表示td */
#submit_error #error_title {
	font-size: 25px;
	font-weight: bold;
	color: #f00;
}

</style>
</head>
<body id="submit_error">
<div id="top"></div>
<table align="center">
 <tr>
  <td id="error_title"><b>$_[0]</b><br></td>
 </tr>
 <tr>
  <td>
  <b>$_[1]</b>
  </td>
 </tr>
 <tr>
  <td>
   <br>

<form action="http://fujiokafix.atumari.net/cgi-bin/mail_studio_enishi/mail.cgi" method="post" novalidate="novalidate">
	<input type="hidden" name="name" value="$param{name}" />
	<input type="hidden" name="kana" value="$param{kana}" />
	<input type="hidden" name="zip1" value="$param{zip1}" />
	<input type="hidden" name="zip2" value="$param{zip2}" />
	<input type="hidden" name="add" value="$param{add}" />
	<input type="hidden" name="tel" value="$param{tel}" />
	<input type="hidden" name="email" value="$param{email}" />
	<input type="hidden" name="email_confirm" value="$param{email_confirm}" />
	<input type="hidden" name="hope" value="$param{hope}"/>
	<input type="hidden" name="msg" value="$param{msg}" />
	<input type="hidden" name="type" value="$param{type}" />
	<input type="hidden" name="place" value="$param{place}" />
	<input type="hidden" name="question" value="$param{question}" />
	<input type="hidden" name="approval" value="true" />
	<input type="submit" value=" 送 信 ">
	<input type="button" value="もどる" onClick="JavaScript:history.back()">
</form>

  </td>
 </tr>
</table>

</body></html>
END
exit;
}

##=====================================
## DICタグの置き換え
##=====================================
# $htmldata = &dicTag(@html);
sub dicTag # (@html)
{
	local(@array) = @_;
	local($data);
	
	$data = '';
	foreach(@array){
		s/_%(.+?)%_/$subst{$1}/g;
		$data .= $_;
	}
	return($data);
}


##=====================================
## ファイルオープン
##=====================================
sub fileopen { # ($filepath)
	local($file, $line) = @_;
	local(@array);
	
	if(!open(IN,$file)){
		stdio::unlock($lock);
		&error('システムエラー',"ファイルをオープンできませんでした。"); }
	@array = <IN>;
	close(IN);
	
	return (@array);
}
