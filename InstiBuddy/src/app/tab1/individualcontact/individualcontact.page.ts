import { Component, OnInit } from '@angular/core';
import { EmailComposer } from '@ionic-native/email-composer/ngx';


@Component({
  selector: 'app-individualcontact',
  templateUrl: './individualcontact.page.html',
  styleUrls: ['./individualcontact.page.scss'],
})
export class IndividualcontactPage implements OnInit {

  constructor(private emailComposer: EmailComposer) {}
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

  ngOnInit() {
  }

}

 
