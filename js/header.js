function header(rootDir){
	var html = "";
	
	html += '	<div id="headerArea">';
	html += '		<div class="left">';
	html += '			<div class="logoBox">';
	html += '				<div class="logoMark">';
	html += '					<a href="http://www.studioenishi.jp/">';
	html += '						<img class="hvr-push" src="img/common/cmn_header_logomark.png" alt="スタジオ縁 造園 緑化 ロゴ" />';
	html += '					</a>';
	html += '				</div>';
	html += '				<div class="logoType">';
	html += '					<a href="http://www.studioenishi.jp/">';
	html += '						<img src="img/common/cmn_header_logotype.png" alt="スタジオ縁 造園 緑化 社名"/>';
	html += '					</a>';
	html += '				</div>';
	html += '			</div>';
	html += '		</div>';
	html += '		<div class="right">';
	html += '			<a href="free.html">';
	html += '				<p class="freeLogo hvr-grow-rotate"></p>';
	html += '			</a>';
	html += '		</div>';
	html += '	</div><!-- /#headerArea -->';
	
	// スマホメニュー
	html += '	<div id="spMenuArea">';
	html += '		<dl id="acMenu">';
	html += '			<dt><i class="icon-reorder"></i>MENU</dt>';
	html += '<dd>';
	html += '					<li><a href="http://www.studioenishi.jp/">トップページ</a></li>';
	html += '					<li><a href="about.html">会社概要</a></li>';
	html += '					<li><a href="green.html">グリーンデザイン</a></li>';
	html += '					<li><a href="works.html">実績の紹介</a></li>';
	html += '					<li><a href="flow.html">ご依頼の流れ</a></li>';
	html += '					<li><a href="employment.html">採用情報</a></li>';
	html += '					<li><a href="contact.html">お問い合わせ</a></li>';
	html += '					<li><a href="free.html">無料設計相談</a></li>';
	html += '				</ul>';
	html += '			</dd>';
	html += '		</dl>';
	html += '	</div>';
	
	// PCメニュー
	html += '	<nav>';
	html += '		<div id="naviRap">';
	html += '			<div id="gNaviArea">';
	html += '				<ul class="gNavi">';
	html += '					<li class="menu5">';
	html += '						<a href="about.html"><span class="menu_head">会</span>社概要<br>';
	html += '							<span class="menu_caption">About</span>';
	html += '						</a>';
	html += '					</li>';
	html += '					<li class="bar"><img src="img/common/cmn_hr.png" /></li>';
	html += '					<li class="menu1">';
	html += '						<a href="green.html"><span class="menu_head">グ</span>リーンデザイン <br>';
	html += '							<span class="menu_caption">Green Design</span>';
	html += '						</a>';
	html += '					</li>';
	html += '					<li class="bar"><img src="img/common/cmn_hr.png" /></li>';
	html += '					<li class="menu2">';
	html += '						<a href="works.html"><span class="menu_head">実</span>績の紹介<br>';
	html += '							<span class="menu_caption">Works</span>';
	html += '						</a>';
	html += '					</li>';
	html += '					<li class="bar"><img src="img/common/cmn_hr.png" /></li>';
	html += '					<li class="menu4">';
	html += '						<a href="flow.html"><span class="menu_head">ご</span>依頼の流れ<br>';
	html += '							<span class="menu_caption">Work Flow</span>';
	html += '						</a>';
	html += '					</li>';
	html += '					<li class="bar"><img src="img/common/cmn_hr.png" /></li>';
	html += '					<li class="menu3">';
	html += '							<a href="employment.html"><span class="menu_head">採</span>用情報<br>';
	html += '							<span class="menu_caption">Employment</span>';
	html += '						</a>';
	html += '					</li>';
	html += '					<li class="bar"><img src="img/common/cmn_hr.png" /></li>';
	html += '					<li class="menu6">';
	html += '						<a href="contact.html"><span class="menu_head">お</span>問い合わせ<br>';
	html += '							<span class="menu_caption">Contact</span>';
	html += '						</a>';
	html += '					</li>';
	html += '				</ul>';
	html += '			</div><!-- /#gNaviArea -->';
	html += '		</div>';
	html += '	</nav>';
	
	
	document.write(html);
}