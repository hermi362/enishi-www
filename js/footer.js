function footer(rootDir){
	var html = "";
	
	// to-top-btn
	html += '	<p class="pageTop"><a href="http://www.studioenishi.jp/" class="hvr-pulse-grow">';
	html += '		<img src="img/common/cmn_pagetop_icon.png">';
	html += '	</a></p>';
	
	// フッターナビエリア
	html += '	<div id="fNaviFrame">';
	html += '		<div id="fNaviArea">';
	html += '			<nav>';
	html += '				<div class="area01">';
	html += '					<ul>';
	html += '						<li><a href="index.html">トップ</a></li>';
	html += '						<li><a href="green.html">スタジオ縁が提案する緑化事業</a></li>';
	html += '						<li><a href="works.html">実績の紹介</a></li>';
	html += '					</ul>';
	html += '				</div>';
	html += '				<div class="area02">';
	html += '					<ul>';
	html += '						<li><a href="flow.html">ご依頼の流れ</a></li>';
	html += '						<li><a href="about.html">会社概要</a></li>';
	html += '						<li><a href="about.html#greeting">代表挨拶</a></li>';
	html += '					</ul>';
	html += '				</div>';
	html += '				<div class="area03">';
	html += '					<ul>';
	html += '						<li><a href="employment.html">採用情報</a></li>';
	html += '						<li><a href="contact.html">お問い合わせ</a></li>';
	html += '						<li><a href="free.html">無料設計相談</a></li>';
	html += '					</ul>';
	html += '				</div>';
	html += '				<div class="area04">';
	html += '					<ul>';
	html += '						<li><a href="privacy.html">プライバシーポリシー</a></li>';
	html += '						<li><a href="copy.html">著作権について</a></li>';
	html += '					</ul>';
	html += '				</div>';
	html += '			</nav>';
	html += '		</div><!-- /#fNaviArea -->';
	html += '	</div><!-- /#fNaviFrame -->';
	
	// フッター
	html += '	<div id="footerArea">';
	html += '		<div class="area01">';
	html += '			<p class="logo03"><a href="http://www.studioenishi.jp/">';
	html += '				<img class="hvr-wobble-top" src="img/common/cmn_footer_logo.png" alt="" />';
	html += '			</a></p>';
	html += '		</div>';
	html += '		<div class="area02">';
	html += '			<ul>';
	html += '				<li class="li01">船橋本社事務所</li>';
	html += '				<li class="li02">〒273-0012　千葉県船橋市浜町1-6ファミリータウン5棟112</li>';
	html += '				<li class="tel"><img src="img/common/cmn_tel_img.png"><span>営業時間 08：00～17：00</span></li>';
	html += '				<li class="li03"><a href="contact.html">ファックスのお客様は会社概要ページより、問い合わせフォームもご用意しております。</a></li>';
	html += '			</ul>';
    html += '		</div>';
	html += '		<div class="area03">';
	html += '			<ul>';
	html += '				<li><a class="hvr-push" href="https://goo.gl/maps/pTZo269LPwkDzq2s7" target="_blank"><p class="access"></p>ｱｸｾｽﾏｯﾌﾟ</a></li>';
	html += '				<li><a class="hvr-push" href="contact.html"><p class="ml"></p></a></li>';
	html += '			</ul>';
	html += '		</div>';
	html += '	</div><!-- /#footerArea -->';

	// コピーライト
	html += '	<div id="copyFrame">';
	html += '		<div id="copyArea">';
	html += '			<p>&copy; 2015 <a href="http://www.studioenishi.jp/">船橋市から全国へ多様な緑化を提案します│株式会社 スタジオ縁</a> All Rights Reserved.</p>';
	html += '		</div><!-- /#copyArea --> ';
	html += '	</div><!-- /#copyFrame -->';
	
	
	document.write(html);
}