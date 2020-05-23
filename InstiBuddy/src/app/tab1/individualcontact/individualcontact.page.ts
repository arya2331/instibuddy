import { Component, OnInit } from '@angular/core';
import { EmailComposer } from '@ionic-native/email-composer/ngx';
import { CallNumber } from '@ionic-native/call-number/ngx';


@Component({
  selector: 'app-individualcontact',
  templateUrl: './individualcontact.page.html',
  styleUrls: ['./individualcontact.page.scss'],
})
export class IndividualcontactPage implements OnInit {

  constructor(private emailComposer: EmailComposer, private callNumber: CallNumber) {}
    public async SendEmail(){
          console.log("hi")
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

  ngOnInit() {
  }

}

 
