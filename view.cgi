#!/usr/local/bin/perl
$ver = "1.3";						#�ύX���Ȃ��ŉ�����
#+------------------------------------------------------------------------
#|View(�C���X�g�\���p�⏕�v���O���� - CGI����)                  1999/ 8/ 8
#|(c)1999 �s�v�c�G�̋�(https://ygkb.jp/)
#|���g����
#| view.cgi?config&imagefile.jpg&imagefile.txt&��i��
#| �|�I�v�V�����̈Ӗ��͈ȉ��̒ʂ� ( & �ŋ�؂��Ă��܂�)�|
#|   1�Ԗ�:�g�p����ݒ�t�@�C�����B
#|   2�Ԗ�:�\������C���[�W�t�@�C���B
#|   3�Ԗ�:���̃C���[�W�t�@�C���̐������B  (�e�L�X�g�̂� SJIS�ŏ�������)
#|   4�Ԗ�:��i�̖��O�B                    (�����ł��ǂ���SJIS�œn������)
#+------------------------------------------------------------------------
#���X�V����
#1.3	Skin�@�\������ / �߂�{�^����t����
#1.2	�ȒP�ȃG���[�����Ƃ��t���� / GET����̓p�X���󂯕t���Ȃ��悤�ɂ���
#1.1	���z�t�H�[���̊ԈႢ���C��
#1.1��	���z�t�H�[����t���Ă݂�
#1.0	�̍ق𐮂���
#0.1	�Ƃ肠�������
#+------------------------------------------------------------------------

### URL�f�R�[�h
@d = split(/&/,$ENV{"QUERY_STRING"});

###�ݒ�ۑ��t�@�C���ďo
require "./def/${d[0]}/${d[0]}.def";


### �h�L�������g�t�@�C���ǂݍ���
if ($d[2] ne "") {												#�t�@�C������[�w�肳��Ă���Ȃ�]
	if (($d[2] =~ /.*\//) || ($d[1] =~ /.*\//)) {				#�O������̑��΃p�X����������Ȃ�
		$d[3] = '�O������̃p�X�w��͋֎~����Ă��܂�';			#�������炪��������x����
		$DoPutForm = 0;
		@data = (
			"\n�n�b�L���O�͂����Ȃ����Ƃł�(;�L�D�M)",
			"���Ȃ��� ���� ���񂵂傤���悤�ˁ��@���ɂ�����Ƃ̂₭�����������@��(�����E)b\n",
			"���ꂩ��A�A�j�����݂�Ƃ��� �ւ�������邭���� �߂� �����Â��Ȃ��悤�ɂ��܂��傤��.",
		);
	} else {
		open(DATA,"${dir_txt}$d[2]");							#�ǂݍ��݃��[�h�ŃI�[�v��
		chop(@data = <DATA>);									#���s�R�[�h�𔲂����
		close(DATA);											#�t�@�C�����N���[�Y
		$Flag_NoDoc = 0;
	}
} else {														#[�w�肳��Ă��Ȃ��Ȃ�]
	$Flag_NoDoc = 1;											#�S�~����菜��(Perl��Ver�Ɉ���H)
}

### ��i�̖��O���w�肳��Ă��Ȃ�������t���O�𗧂Ă�
if ($d[3] eq "") { $Flag_NoName = 1; }


### HTML�o��1
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


### ���O���w�肳��Ă��Ȃ��������i�^�C�g���͕\�����Ȃ�
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


### ���O���w�肳��Ă��Ȃ��������i�^�C�g���͕\�����Ȃ�
unless ($Flag_NoName) { print "<CENTER><FONT SIZE=+2><B>��$d[3]��</B></FONT></CENTER>\n\n<BR><HR><BR>\n\n"; }


### �G��\��
if ($DoPutWaku) {				#�g��\������Ȃ�
	if ($DoPutTable) {			#�Â����g��\������Ȃ�

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

	} else {					#���ʂ̃e�[�u���ŗǂ��Ȃ�
		print "<CENTER><TABLE BORDER=$thick[0]><TR><TD><IMG SRC=\"${dir_img}$d[1]\" ALT=\"$d[3]\"></TD></TR></TABLE></CENTER><BR>";
	}
} else {						#�g��\�����Ȃ��Ȃ�
	print "<CENTER><IMG SRC=\"${dir_img}$d[1]\" ALT=\"$d[3]\"></CENTER><BR>";
}


### �h�L�������g�t�@�C�����w�肳��Ă���Ȃ�\�����ėǂ�
unless ($Flag_NoDoc) {
	print "<CENTER><TABLE BORDER=0><TR><TD $tblbg[0]><PRE>\n";


	### �v���[���e�L�X�g�\���t�B���^
	foreach $line (@data) {
		$line =~ s/&/&amp;/g;
		$line =~ s/"/&quot;/g;
		$line =~ s/</&lt;/g;
		$line =~ s/>/&gt;/g;
		print $line."\n";
	}


	### HTML�o��2
	print "</PRE></FONT></TD></TR></TABLE></CENTER>\n\n";
}


### �t�H�[���̕\�����w�肳��Ă���Ȃ�\�����ėǂ�
if ($DoPutForm) {
print <<"END";

<!-- ���z�t�H�[�� -->
<TABLE BORDER=0 CELLSPACING=2 CELLPADDING=6 ALIGN=center>
	<TR><TD ALIGN=center COLSPAN=2>
	<B><FONT COLOR=#6f55ff>
		<FONT SIZE=+2>�����ɂł����犴�z����������(^^)��</FONT><BR>
		(Please send your impression!(^^))<BR><BR>
		�������A�����_�ł͐V���߂̃u���E�U�ł�������܂���B<BR>
		(But , you have to use IE4.0 NN3.0 later)
	</B></FONT>
	</TD></TR>

	<FORM ACTION=\"mailto:$addr\" METHOD=POST>

	<TR>
		<TD $tblbg[1]><B>�����O</B>(�����ł͂���܂���)<BR><B>NAME</B> (It's up to you whether you write this)</TD>
		<TD $tblbg[2]><INPUT TYPE=text NAME=name SIZE=40 MAXLENGS=60></TD>
	</TR>

	<TR>
		<TD $tblbg[1]><B>���[���A�h���X</B>(�����ł͂���܂���)<BR><B>E-MAIL Address</B> (It's up to you whether you write this)</TD>
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

print "\n<BR><BR><HR><BR>\n<CENTER><A HREF=\"$ENV{'HTTP_REFERER'}\"><FONT SIZE=+1>���߂遜</FONT></A></CENTER><BR>\n";
print "\n<HR>\n<DIV ALIGN=right><A HREF=\"https://ygkb.jp/\">View $ver by Enogu Fukashigi</A></DIV>\n</BODY></HTML>\n";

end;
