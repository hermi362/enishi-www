#!/usr/local/bin/perl --

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\  Creation company : DIC Inc.
#\\  http://www.d-ic.com/
#\\  DIC-Studio. Mail_v2s Version:1.82 (2012/09/07)
#\\  Copyright (C) DIC All Rights Reserved. ���̃X�N���v�g�̍Ĕz�z�Ȃǂ��֎~���܂�.
#\\  �o�O�񍐂� studio@d-ic.com ���ɂ��肢���܂��B
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

##*****<< �ݒu���@ >>******************************************************************************
##
## ���b�f�h�t�@�C���̏����ݒ�����g���̊��ɍ��킹�ăJ�X�^�}�C�Y���Ă��������B
## �����g���̃T�[�o�ɂ���Ă͉��̃t�@�C���\���ł͓��삵�Ȃ��ꍇ������܂��B
##   ���̍ۂ̓T�[�o�Ǘ��҂ɂ��₢���킹���������B
## ��"[]"���̐����̓p�[�~�b�V�����ł��B
## ��"form.html"�́A������"sample.html"���Q�l�ɍ쐬���Ă��������B
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
##*****<< �o�[�W�����A�b�v��� >>******************************************************************
##
## 2012/09/07 .....Ver1.82
##   �E�����ԐM���[���̌��������R�ɐݒ�ł���悤�ɉ��ǁB
##   �E�����ɓ��͒l���������ދ@�\��ǉ��B
##
## 2007/05/09 .....Ver1.8
##   �E�Z�L�����e�B�΍�
##
## 2007/05/08 .....Ver1.7
##   �E���M���[���A�h���X�A���[�������A�K�{���ځA���M�����y�[�W��URL�A��mail.cgi�ɂĐݒ肷��悤�ɏC���B
##
## 2004/12/05 .....Ver1.6
##   �E����name�����������������ꍇ�ɏd�����Ă��܂��o�O���C���B
##
## 2003/07/11 .....Ver1.5
##   �E���̓t�H�[���ɂ�Email���ȗ������ꍇ�G���[���N�����o�O���C���B
##
## 2003/06/02 .....Ver1.40
##   �E�t�H�[���̃y�[�W�� �K�{���ځA���M�����y�[�W�A���M��A���� ���w��ł���悤�ɏC���B
##   �E���M�������ɔC�ӂ̃y�[�W�փW�����v�ł���悤�ɋ@�\�ǉ��B�i�e���v���[�g�Ƃ��ēǂݍ��ނ̂ł͂Ȃ��A�W�����v����悤�ɏC���j
##   �E�e���v���[�g�g�s�l�k�Ȃǂׂ̍����C��
##
## 2002/12/11 .....Ver1.30
##   �E���M��Ƀz�[���y�[�W�ɖ߂��悤�Ƀ����N��\��@�\��ǉ�
##   �E�e���v���[�g�g�s�l�k�Ȃǂׂ̍����C��
##
## 2002/10/03 .....Ver1.20
##   �E�e���v���[�g�g�s�l�k�Ȃǂׂ̍����C��
##
##*************************************************************************************************


##=====================================
##           �����ݒ蕔��             =
##=====================================

# ���M���[���A�h���X
$mailaddress = 'enishi.office@gmail.com';


# ����
# ���̂悤�ɁA�u_%name�l%_�v��}�����邱�ƂŁA���͏����������ނ��Ƃ��ł��܂��B
# $subject = '[_%�����O%_����]HP����⍇��';

# �Ǘ��҈�	'[_%name%_����]HP����⍇��';
$subject = 'HP����⍇��';

# ���[�U��
$re_subject = '���⍇�����肪�Ƃ��������܂�';


# ���͕K�{����
@necessary = ('name','kana','zip1','zip2','add','tel','email','email_confirm','approval');

# ���M������ʂ�URL
$thank_page = '';

# sendmail�̃p�X
$sendmail = '/usr/sbin/sendmail';

# �e���v���[�g�i�����ԐM���[���̖{���j
#$remail_txt = './remail.txt';

# �e���v���[�g�g�s�l�k�i���͊m�F�p�j
$template1 = './check.html';

# �m�F��ʂ̃e�[�u���f�U�C��
$tablewidth = '650';		# �e�[�u���̉���
$bgcolor1 = '#FFFFFF';		# ���ڂ̐F
$bgcolor2 = '#FFFFFF';		# ���e�̐F
$border = '0';				# �g���̑����i�Ȃ�=0�j
$bordercolor = '#999999';	# �g���̐F
$cellpadding = '0';			# cellpadding



##=====================================
## �T�u���[�`��                       =
##=====================================
require './jcode.pl';
require './stdio.pl';



#������������������������ �������牺���C�������ꍇ�ɂ̓T�|�[�g�ΏۊO�ɂȂ�܂��B�����ӂ��������B ����������������������

##=====================================
## �f�[�^���󂯎��                   =
##=====================================
%param = ();
@key_list = stdio::getFormData(\%param,0,sjis,1," \/ ",);





#�������������������������������������� ���[�h�w�� "�Ȃ�" ����������������������������������������������
if(!$param{'mode'}){


if($param{'email'} ne $param{'email_confirm'}) {
	&error('���̓G���[',"���[���A�h���X����v���܂���<BR><BR>$param{'email'}<BR>$param{'email_confirm'}");
}

##=====================================
## �K�{���ڂ̓��̓`�F�b�N             =
##=====================================
foreach(@necessary){

	if(!$param{$_}){
		if($_ eq 'name') {
			$hissu_check .= "�E�����O<br>";
		} elsif($_ eq 'kana') {
			$hissu_check .= "�E�t���K�i<br>";
		} elsif($_ eq 'zip1') {
			$hissu_check .= "�E�X�֔ԍ�(�O)<br>";
		} elsif($_ eq 'zip2') {
			$hissu_check .= "�E�X�֔ԍ�(��)<br>";
		} elsif($_ eq 'add') {
			$hissu_check .= "�E���Z��<br>";
		} elsif($_ eq 'tel') {
			$hissu_check .= "�E�d�b�ԍ�<br>";
		} elsif($_ eq 'email') {
			$hissu_check .= "�E���[���A�h���X<br>";
		} elsif($_ eq 'email_confirm') {
			$hissu_check .= "�E���[���A�h���X(�m�F�p)<br>";
		} elsif($_ eq 'approval') {
			$template1 = './check_approval.html';
			#&error_not_approval('���̓G���[', "�u�l���̎�舵���ɂ��āv�̓��ӂ���`�F�b�N�{�b�N�X�Ƀ`�F�b�N�T�C��������Ă��܂���A���b�Z�[�W�₨�₢���킹���e�͑��M����܂����ԓ��Ɋւ��Ă̓`�F�b�N�T�C�������ꂽ���݂̂Ƃ����Ē������������������������B<BR><BR>�����͂������e���m�F���Ă��������A��L���e�ɂĂ�낵����� ���M�{�^�� ���N���b�N���Ă��������B<BR>");
		}
	}
}

if($hissu_check){ &error('���̓G���[',"�ȉ��̕K�{���ڂɓ��͂�����܂���ł����B<br><br>$hissu_check"); }


##=====================================
## E���[�����͂̃`�F�b�N              =
##=====================================
if($param{'email'}){
	if($param{'email'} =~ /^\S+@\S+\.\S+/){ ; }
	else{ &error('���̓G���[',"E���[���A�h���X�̓��͂��ԈႦ�Ă��܂��B"); }
	if($param{'email'} =~ /�`|�a|�b|�c|�d|�e|�f|�g|�h|�i|�j|�k|�l|�m|�n|�o|�p|�q|�r|�s|�t|�u|�v|�w|�x|�y/){ &error('���̓G���[',"E���[���A�h���X�̓��͂��ԈႦ�Ă��܂��B���p�p�������g�p���Ă��������B"); }
	if($param{'email'} =~ /��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��|��/){ &error('���̓G���[',"E���[���A�h���X�̓��͂��ԈႦ�Ă��܂��B���p�p�������g�p���Ă��������B"); }
	if($param{'email'} =~ /[^\-\.\@\_0-9a-zA-Z]/){ &error('�G���[','���͂��ԈႦ�Ă��܂��B'); }
}


##=====================================
## ����L����ϊ�����                 =
##=====================================
foreach (@key_list) {
	$param{$_} =~ s/&/��/g;
	$param{$_} =~ s/\"/�h/g;
	$param{$_} =~ s/</��/g;
	$param{$_} =~ s/>/��/g;
	$param{$_} =~ s/,/�C/g;
	$param{$_} =~ s/\'/�f/g;
	$param{$_} =~ s/\n/ /g;
}


##=====================================
## ���͊m�F��ʂ̈ꕔ                 =
##=====================================
@key_list = grep(!$seen{$_}++, @key_list);

foreach(@key_list){

	&jcode::convert(\$param{\$_},'Shift_JIS');

	if($_ eq 'submit'){ next; }
	
	if($_ eq 'name'){
		$title_name = '�����O';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"�����O\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'kana') {
		$title_name = '�t���K�i';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"�t���K�i\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'zip1') {
		$title_name = '�X�֔ԍ�';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}-$param{'zip2'}<input type=\"hidden\" name=\"�X�֔ԍ�\" value=\"$param{$_}-$param{zip2}\"></td></tr>";
	} elsif($_ eq 'add') {
		$title_name = '���Z��';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"���Z��\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'tel') {
		$title_name = '�d�b�ԍ�';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"�d�b�ԍ�\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'email') {
		$title_name = '���[���A�h���X';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"���[���A�h���X\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'hope') {
		$title_name = '��]�̘A����i';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"��]�̘A����i\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'msg') {
		$title_name = '���⍇�����e';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"���⍇�����e\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'type') {
		$title_name = '�Ή��̎��';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"�Ή��̎��\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'place') {
		$title_name = '�Ή��\��ꏊ';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"�Ή��\��ꏊ\" value=\"$param{$_}\"></td></tr>";
	} elsif($_ eq 'question') {
		$title_name = '����E�v�]��';
		$mail_table .= "\n<tr><td class=\"title\">$title_name</td><td id=\"text\">$param{$_}<input type=\"hidden\" name=\"����E�v�]��\" value=\"$param{$_}\"></td></tr>";
	}

	#if($param{$_}){ $param = $param{$_}; }
}


$mail = qq|
<input type="hidden" name="mode" value="mailsend">


   $mail_table

|;


##=====================================
## �m�F�e���v���[�g�t�@�C�����I�[�v�� =
##=====================================
if(!open(HTML,$template1)){ &error('�V�X�e���G���[',"�e���v���[�g�t�@�C�� ( $template1 ) ���I�[�v���ł��܂���B");}
@html = <HTML>;
close(HTML);


##=====================================
## ���ꕶ����u������                 =
##=====================================
$dic = qq|<div align="right" class="copyright">- <a href="http://www.d-ic.com/" target="_top">���[�����M�v���O�����F DIC-Studio</a> -</div>|;
foreach(@html){
	if($_ =~ /_%copyright%_/){ $flag = '1'; }
	s/_%mail%_/$mail/g;
	s/_%Email%_/$mailaddress/g;
	s/_%copyright%_/$dic/g;
}
if(!$flag){ &error('�V�X�e���G���[',''); }


##=====================================
## �m�F��ʕ\��                       =
##=====================================
print <<"EOF";
Content-type: text/html

@html
EOF
exit;
}	# ���[�h�w�� �Ȃ� �����܂�


#�������������������������������������� ���[�h�w�� "mailsend" ����������������������������������������������
if($param{'mode'} eq 'mailsend'){

##=====================================
## ����L����ϊ�����                 =
##=====================================
foreach (@key_list) {
	$param{$_} =~ s/\n/ /g;
	$param{$_} =~ s/&/��/g;
	$param{$_} =~ s/\"/�h/g;
	$param{$_} =~ s/</��/g;
	$param{$_} =~ s/>/��/g;
	$param{$_} =~ s/,/�C/g;
	$param{$_} =~ s/\'/�f/g;
	
	$subst{$_} = $param{$_};
}


##=====================================
## ���[������
##=====================================
@subject = ($subject);
@re_subject = ($re_subject);

$subject = &dicTag(@subject);
$re_subject = &dicTag($re_subject);


##=====================================
## ���[���{��                         =
##=====================================
$mailbody = "$subject\n\n";

foreach(@key_list){
	if($_ eq 'mode'){ next; }
#	elsif($_ eq 'remail'){ next;}
	
	$mailbody .= "��$_\n$param{$_}\n\n";
#	$remailbody .= "\n��$_\n$param{$_}\n";
}


##=====================================
## ���[�����M                         =
##=====================================
if($param{'email'}){ $mailfrom = $param{'email'}; }
else{ $mailfrom = 'xxxxx@xxxx.xxx'; }

%header = (
    'To'      => $mailaddress,
    'From'    => $mailfrom,
    'Subject' => $subject
);
$result = stdio::sendmail($sendmail, \%header,$mailbody, 0, 0,);
if(!$result){ &error('�V�X�e���G���[',"���[���̑��M�Ɏ��s���܂����B"); }

##=====================================
## ���[�����M�����\��                 =
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
<title>���[���t�H�[��</title>
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
    <h2>���M����</h2>
    <br><br><br><br><br><br>
</div>
</body>
</html>
EOF
exit;
}
}	# ���[�h�w�� mailsend �����܂�


##=====================================
## �G���[�\��                         =
##=====================================
sub error {
print <<"END";
Content-type: text/html

<html><head><title>!ERROR!</title>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<style type="text/css">

/* �w�i�ݒ� */
body#submit_error {
	background-image: url(http://fujiokafix.atumari.net/template/bg2.jpg);
	background-size: cover;
	background-position: 50% 0;
	height: 100%;
}
/* �����N */
#submit_error a {
  color: #000;
  text-decoration: none;
}
#submit_error a:hover {
	color: #33A400;
}
/* �G���[���ڕ\���e�[�u���ݒ� */
#submit_error table {
  width: 660px;
  border-width: 0px;
	margin-top: 50px;
}
#submit_error td { 
	font-size: 14px;
}
/* �u���̓G���[�v�\��td */
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
    <p><a href="JavaScript:history.back()">��������N���b�N���đO�̉�ʂɈړ����Ă��������B</a>
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

#-- ���Ӄ`�F�b�N������ĂȂ������ꍇ --#
sub error_not_approval {
print <<"END";
Content-type: text/html

<html><head><title>!ERROR!</title>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<style type="text/css">

/* �w�i�ݒ� */
body#submit_error {
	background-image: url(http://fujiokafix.atumari.net/template/bg2.jpg);
	background-size: cover;
	background-position: 50% 0;
	height: 100%;
}
/* �����N */
#submit_error a {
  color: #000;
  text-decoration: none;
}
#submit_error a:hover {
	color: #33A400;
}
/* �G���[���ڕ\���e�[�u���ݒ� */
#submit_error table {
  width: 660px;
  border-width: 0px;
	margin-top: 50px;
}
#submit_error td { 
	font-size: 14px;
}
/* �u���̓G���[�v�\��td */
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
	<input type="submit" value=" �� �M ">
	<input type="button" value="���ǂ�" onClick="JavaScript:history.back()">
</form>

  </td>
 </tr>
</table>

</body></html>
END
exit;
}

##=====================================
## DIC�^�O�̒u������
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
## �t�@�C���I�[�v��
##=====================================
sub fileopen { # ($filepath)
	local($file, $line) = @_;
	local(@array);
	
	if(!open(IN,$file)){
		stdio::unlock($lock);
		&error('�V�X�e���G���[',"�t�@�C�����I�[�v���ł��܂���ł����B"); }
	@array = <IN>;
	close(IN);
	
	return (@array);
}
