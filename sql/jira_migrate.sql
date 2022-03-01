INSERT INTO jira_nord_terms VALUES('nationalexpress');
INSERT INTO jira_nord_terms VALUES('accuweather');
INSERT INTO jira_nord_terms VALUES('destinia');
INSERT INTO jira_nord_terms VALUES('holidaycheck');
INSERT INTO jira_nord_terms VALUES('lmn');
INSERT INTO jira_nord_terms VALUES('lastminute');
INSERT INTO jira_nord_terms VALUES('guestreservations');
INSERT INTO jira_nord_terms VALUES('guestres');
INSERT INTO jira_nord_terms VALUES('esky');
INSERT INTO jira_nord_terms VALUES('ostrovok');
INSERT INTO jira_nord_terms VALUES('weather');
INSERT INTO jira_nord_terms VALUES('united airlines');
INSERT INTO jira_nord_terms VALUES('ticketoffices');
INSERT INTO jira_nord_terms VALUES('logitravel');
INSERT INTO jira_nord_terms VALUES('tuifly');
INSERT INTO jira_nord_terms VALUES('leafgroup');
INSERT INTO jira_nord_terms VALUES('directferries');
INSERT INTO jira_nord_terms VALUES('realclearpolitics');
INSERT INTO jira_nord_terms VALUES('boxofficeticket');
INSERT INTO jira_nord_terms VALUES('spirit');
INSERT INTO jira_nord_terms VALUES('lajollamom');
INSERT INTO jira_nord_terms VALUES('volagratis');
INSERT INTO jira_nord_terms VALUES('wetter');
INSERT INTO jira_nord_terms VALUES('weg');
INSERT INTO jira_nord_terms VALUES('rumbo');
INSERT INTO jira_nord_terms VALUES('bravofly');
INSERT INTO jira_nord_terms VALUES('ask');
INSERT INTO jira_nord_terms VALUES('hotelplanner');
INSERT INTO jira_nord_terms VALUES('secretescapes');
INSERT INTO jira_nord_terms VALUES('megabus');
INSERT INTO jira_nord_terms VALUES('iwantthatflight');
INSERT INTO jira_nord_terms VALUES('nypost');
INSERT INTO jira_nord_terms VALUES('10best');
INSERT INTO jira_nord_terms VALUES('tripadvisor');
INSERT INTO jira_nord_terms VALUES('priceline');
INSERT INTO jira_nord_terms VALUES('rvshare');
INSERT INTO jira_nord_terms VALUES('mapquest');
INSERT INTO jira_nord_terms VALUES('hotels.com');
INSERT INTO jira_nord_terms VALUES('fix');
INSERT INTO jira_nord_terms VALUES('bug');

INSERT INTO jira_nord_terms VALUES('nationalrail');
INSERT INTO jira_nord_terms VALUES('booking.com');
INSERT INTO jira_nord_terms VALUES('falk');
INSERT INTO jira_nord_terms VALUES('10times');
INSERT INTO jira_nord_terms VALUES('liligo');
INSERT INTO jira_nord_terms VALUES('expedia');
INSERT INTO jira_nord_terms VALUES('weekendesk');
INSERT INTO jira_nord_terms VALUES('ticketsales');
INSERT INTO jira_nord_terms VALUES('error');
INSERT INTO jira_nord_terms VALUES('petitefute.com');
INSERT INTO jira_nord_terms VALUES('viamichelin ');
INSERT INTO jira_nord_terms VALUES('swoodoo ');
INSERT INTO jira_nord_terms VALUES('kayak');
INSERT INTO jira_nord_terms VALUES('look into');
INSERT INTO jira_nord_terms VALUES('jetcost');
INSERT INTO jira_nord_terms VALUES('jet cost');
INSERT INTO jira_nord_terms VALUES('hotwire');
INSERT INTO jira_nord_terms VALUES('travelocity');
INSERT INTO jira_nord_terms VALUES('orbitz');
INSERT INTO jira_nord_terms VALUES('trivago');
INSERT INTO jira_nord_terms VALUES('cheapflights');
INSERT INTO jira_nord_terms VALUES('loveholiday');
INSERT INTO jira_nord_terms VALUES('momondo');
INSERT INTO jira_nord_terms VALUES('marriott');
INSERT INTO jira_nord_terms VALUES('tripsavvy');

INSERT INTO jira_nord_terms VALUES('cheapoair');

INSERT INTO jira_nord_terms VALUES('investigate');
INSERT INTO jira_nord_terms VALUES('audit / patch');
INSERT INTO jira_nord_terms VALUES('turn off');
INSERT INTO jira_nord_terms VALUES('live_critical');
INSERT INTO jira_nord_terms VALUES('virail');
INSERT INTO jira_nord_terms VALUES('fpcs - certs and cdn');
INSERT INTO jira_nord_terms VALUES('mapcarta');
INSERT INTO jira_nord_terms VALUES('travelpricedrops');
INSERT INTO jira_nord_terms VALUES('skyscanner');
INSERT INTO jira_nord_terms VALUES('set up campaigns');
INSERT INTO jira_nord_terms VALUES('fodors ');
INSERT INTO jira_nord_terms VALUES('wanderu');
INSERT INTO jira_nord_terms VALUES('findhotel');
INSERT INTO jira_nord_terms VALUES('save70');

INSERT INTO jira_nord_terms VALUES('turismocity ');
INSERT INTO jira_nord_terms VALUES('norton');
INSERT INTO jira_nord_terms VALUES('airbnb');
INSERT INTO jira_nord_terms VALUES('bestday');
INSERT INTO jira_nord_terms VALUES('otelz');
INSERT INTO jira_nord_terms VALUES('hotelscan');
INSERT INTO jira_nord_terms VALUES('vrbo');
INSERT INTO jira_nord_terms VALUES('busbud');
INSERT INTO jira_nord_terms VALUES('bcom');
INSERT INTO jira_nord_terms VALUES('easyvoyage');
INSERT INTO jira_nord_terms VALUES('pcln');
INSERT INTO jira_nord_terms VALUES('block');
INSERT INTO jira_nord_terms VALUES('otelz');
INSERT INTO jira_nord_terms VALUES('85off.com');
INSERT INTO jira_nord_terms VALUES('westworld.com');
INSERT INTO jira_nord_terms VALUES('lola');
INSERT INTO jira_nord_terms VALUES('credentials');
INSERT INTO jira_nord_terms VALUES('icelolly');
INSERT INTO jira_nord_terms VALUES('airbnb');
INSERT INTO jira_nord_terms VALUES('mundi');
INSERT INTO jira_nord_terms VALUES('farecompare ');
INSERT INTO jira_nord_terms VALUES('flighthub ');
INSERT INTO jira_nord_terms VALUES('fodors ');
INSERT INTO jira_nord_terms VALUES('wikitravel ');
INSERT INTO jira_nord_terms VALUES('cozycozy');
INSERT INTO jira_nord_terms VALUES('graphicbomb ');
INSERT INTO jira_nord_terms VALUES('snackmedia');
INSERT INTO jira_nord_terms VALUES('graphic bomb');
INSERT INTO jira_nord_terms VALUES('boston ai');
INSERT INTO jira_nord_terms VALUES('pas config for');
INSERT INTO jira_nord_terms VALUES('trip.com');
INSERT INTO jira_nord_terms VALUES('fpcs - dns records');
INSERT INTO jira_nord_terms VALUES('lonelyplanet ');
INSERT INTO jira_nord_terms VALUES('fluege.de');
INSERT INTO jira_nord_terms VALUES('southwest');
INSERT INTO jira_nord_terms VALUES('fpcs setup for');
INSERT INTO jira_nord_terms VALUES('new account setup for');
INSERT INTO jira_nord_terms VALUES('new hire accounts');
INSERT INTO jira_nord_terms VALUES('aws account setup for');
INSERT INTO jira_nord_terms VALUES('add shaun to sudoers');
INSERT INTO jira_nord_terms VALUES('permissions');
INSERT INTO jira_nord_terms VALUES('hometogo');
INSERT INTO jira_nord_terms VALUES('telegraph');
INSERT INTO jira_nord_terms VALUES('united');
INSERT INTO jira_nord_terms VALUES('viajala ');

INSERT into jira_status(id, status_name_from, status_from, status_name_to, status_to, issue_id, created_date , author_id, author_name )
		select id
					, case when items_0_field_name = 'status' then items_0_from_text
						when items_1_field_name = 'status' then items_1_from_text
						when items_2_field_name = 'status' then items_2_from_text
						when items_3_field_name = 'status' then items_3_from_text
						when items_4_field_name = 'status' then items_4_from_text			
					end as status_name_from
					, case when items_0_field_name = 'status' then items_0_from
						when items_1_field_name = 'status' then items_1_from
						when items_2_field_name = 'status' then items_2_from
						when items_3_field_name = 'status' then items_3_from
						when items_4_field_name = 'status' then items_4_from		
					end as status_from
					, case when items_0_field_name = 'status' then items_0_to_text
						when items_1_field_name = 'status' then items_1_to_text
						when items_2_field_name = 'status' then items_2_to_text
						when items_3_field_name = 'status' then items_3_to_text
						when items_4_field_name = 'status' then items_4_to_text			
					end as status_name_to
					, case when items_0_field_name = 'status' then items_0_to
						when items_1_field_name = 'status' then items_1_to
						when items_2_field_name = 'status' then items_2_to
						when items_3_field_name = 'status' then items_3_to
						when items_4_field_name = 'status' then items_4_to	
					end as status_to
				, issue_id
				, created_date 
				, author_id
				, author_name
			from jira_changelog 
			where items_0_field_name = 'status'
				or items_1_field_name = 'status'
					or items_2_field_name = 'status'
						or items_3_field_name = 'status'
							or items_4_field_name = 'status'
							
							
							
INSERT INTO jira_support_issues VALUES('CREATIVES-27');
INSERT INTO jira_support_issues VALUES('CREATIVES-33');
INSERT INTO jira_support_issues VALUES('ILV-3596');
INSERT INTO jira_support_issues VALUES('ILV-3734');
INSERT INTO jira_support_issues VALUES('ILV-3767');
INSERT INTO jira_support_issues VALUES('ILV-3932');
INSERT INTO jira_support_issues VALUES('ILV-4082');
INSERT INTO jira_support_issues VALUES('ILV-4094');
INSERT INTO jira_support_issues VALUES('ILV-4096');
INSERT INTO jira_support_issues VALUES('ILV-4103');
INSERT INTO jira_support_issues VALUES('ILV-4127');
INSERT INTO jira_support_issues VALUES('ILV-4148');
INSERT INTO jira_support_issues VALUES('ILV-4152');
INSERT INTO jira_support_issues VALUES('ILV-4155');
INSERT INTO jira_support_issues VALUES('ILV-4170');
INSERT INTO jira_support_issues VALUES('ILV-4171');
INSERT INTO jira_support_issues VALUES('ILV-4174');
INSERT INTO jira_support_issues VALUES('ILV-4176');
INSERT INTO jira_support_issues VALUES('ILV-4184');
INSERT INTO jira_support_issues VALUES('ILV-4185');
INSERT INTO jira_support_issues VALUES('ILV-4186');
INSERT INTO jira_support_issues VALUES('ILV-4192');
INSERT INTO jira_support_issues VALUES('ILV-4193');
INSERT INTO jira_support_issues VALUES('ILV-4202');
INSERT INTO jira_support_issues VALUES('ILV-4204');
INSERT INTO jira_support_issues VALUES('ILV-4205');
INSERT INTO jira_support_issues VALUES('ILV-4208');
INSERT INTO jira_support_issues VALUES('ILV-4209');
INSERT INTO jira_support_issues VALUES('ILV-4212');
INSERT INTO jira_support_issues VALUES('ILV-4219');
INSERT INTO jira_support_issues VALUES('ILV-4231');
INSERT INTO jira_support_issues VALUES('ILV-4233');
INSERT INTO jira_support_issues VALUES('ILV-4260');
INSERT INTO jira_support_issues VALUES('ILV-4262');
INSERT INTO jira_support_issues VALUES('ILV-4275');
INSERT INTO jira_support_issues VALUES('ILV-4284');
INSERT INTO jira_support_issues VALUES('ILV-4289');
INSERT INTO jira_support_issues VALUES('ILV-4293');
INSERT INTO jira_support_issues VALUES('ILV-4305');
INSERT INTO jira_support_issues VALUES('ILV-4309');
INSERT INTO jira_support_issues VALUES('ILV-4330');
INSERT INTO jira_support_issues VALUES('ILV-4681');
INSERT INTO jira_support_issues VALUES('ILV-4736');
INSERT INTO jira_support_issues VALUES('ILV-4742');
INSERT INTO jira_support_issues VALUES('ILV-4763');
INSERT INTO jira_support_issues VALUES('ILV-4766');
INSERT INTO jira_support_issues VALUES('ILV-4770');
INSERT INTO jira_support_issues VALUES('ILV-4773');
INSERT INTO jira_support_issues VALUES('ILV-4774');
INSERT INTO jira_support_issues VALUES('ILV-4778');
INSERT INTO jira_support_issues VALUES('ILV-4783');
INSERT INTO jira_support_issues VALUES('ILV-4785');
INSERT INTO jira_support_issues VALUES('ILV-4790');
INSERT INTO jira_support_issues VALUES('ILV-4830');
INSERT INTO jira_support_issues VALUES('ILV-4833');
INSERT INTO jira_support_issues VALUES('ILV-4840');
INSERT INTO jira_support_issues VALUES('ILV-4842');
INSERT INTO jira_support_issues VALUES('ILV-4844');
INSERT INTO jira_support_issues VALUES('ILV-4845');
INSERT INTO jira_support_issues VALUES('ILV-4852');
INSERT INTO jira_support_issues VALUES('ILV-4854');
INSERT INTO jira_support_issues VALUES('ILV-4857');
INSERT INTO jira_support_issues VALUES('ILV-4860');
INSERT INTO jira_support_issues VALUES('ILV-4861');
INSERT INTO jira_support_issues VALUES('ILV-4863');
INSERT INTO jira_support_issues VALUES('ILV-4866');
INSERT INTO jira_support_issues VALUES('ILV-4871');
INSERT INTO jira_support_issues VALUES('ILV-4874');
INSERT INTO jira_support_issues VALUES('ILV-4879');
INSERT INTO jira_support_issues VALUES('ILV-4880');
INSERT INTO jira_support_issues VALUES('ILV-4891');
INSERT INTO jira_support_issues VALUES('ILV-4893');
INSERT INTO jira_support_issues VALUES('ILV-4895');
INSERT INTO jira_support_issues VALUES('ILV-4896');
INSERT INTO jira_support_issues VALUES('ILV-4900');
INSERT INTO jira_support_issues VALUES('ILV-4906');
INSERT INTO jira_support_issues VALUES('ILV-4911');
INSERT INTO jira_support_issues VALUES('ILV-4944');
INSERT INTO jira_support_issues VALUES('ILV-4947');
INSERT INTO jira_support_issues VALUES('ILV-4949');
INSERT INTO jira_support_issues VALUES('ILV-4952');
INSERT INTO jira_support_issues VALUES('INF-1104');

INSERT INTO jira_support_issues VALUES('IEN-1763');
INSERT INTO jira_support_issues VALUES('IEN-1863');
INSERT INTO jira_support_issues VALUES('IEN-1964');
INSERT INTO jira_support_issues VALUES('IEN-2013');
INSERT INTO jira_support_issues VALUES('IEN-2014');
INSERT INTO jira_support_issues VALUES('IEN-2024');
INSERT INTO jira_support_issues VALUES('IEN-2032');
INSERT INTO jira_support_issues VALUES('IEN-2059');
INSERT INTO jira_support_issues VALUES('IEN-2064');
INSERT INTO jira_support_issues VALUES('IEN-2065');

INSERT INTO jira_support_issues VALUES('BAC-5670');
INSERT INTO jira_support_issues VALUES('PLAT-1423');
INSERT INTO jira_support_issues VALUES('PLAT-1429');
INSERT INTO jira_support_issues VALUES('PLAT-1437');
INSERT INTO jira_support_issues VALUES('PLAT-1455');
INSERT INTO jira_support_issues VALUES('PLAT-1458');
INSERT INTO jira_support_issues VALUES('PLAT-1466');
INSERT INTO jira_support_issues VALUES('BAC-4137');
INSERT INTO jira_support_issues VALUES('BAC-3947');
INSERT INTO jira_support_issues VALUES('BAC-4328');



