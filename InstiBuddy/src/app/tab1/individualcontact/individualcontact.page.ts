import { Component, OnInit } from '@angular/core';
import { EmailComposer } from '@ionic-native/email-composer/ngx';
import { CallNumber } from '@ionic-native/call-number/ngx';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NavController } from '@ionic/angular';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-individualcontact',
  templateUrl: './individualcontact.page.html',
  styleUrls: ['./individualcontact.page.scss'],
})
export class IndividualcontactPage implements OnInit {
  public baseURL;
  public url;
  name: string;
  response: Object;
  constructor(private activatedRoute:ActivatedRoute, public navCtrl: NavController, public httpClient: HttpClient,private emailComposer: EmailComposer, private callNumber: CallNumber) {
    this.baseURL='http://localhost:8000/scrapdata/name/';
    this.response={
      "prof_Name":'',
      "phone_number":'',
      "email":'',
      "department":''
    }
  }
  public async SendEmail(){

        //Now we know we can send
        let email = {
          to: 'max@mustermann.de',
          cc: 'erika@mustermann.de',
          bcc: ['john@doe.com', 'jane@doe.com'],
          attachments: [

          ],
          subject: 'Cordova Icons',
          body: 'How are you? Nice greetings from Leipzig',
          isHtml: true
        }
        this.emailComposer.open(email);
      

  };

  public async Call(){
    
    this.callNumber.callNumber("18001010101", true)
    .then(res => console.log('Launched dialer!', res))
    .catch(err => console.log('Error launching dialer', err));
  };
  get(){
    let data={
        "name":this.name
    }
    const httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'}),
      }
    this.httpClient.post(this.baseURL,JSON.stringify(data),httpOptions).subscribe((res1)=>{
      console.log(res1); 
      this.response=res1[0];
    },(error:any)=>{console.log(error); });
    
  }

  ngOnInit() {
    this.name=this.activatedRoute.snapshot.paramMap.get('profcontact');
    console.log(this.name)
    this.get()
  }

}

 
