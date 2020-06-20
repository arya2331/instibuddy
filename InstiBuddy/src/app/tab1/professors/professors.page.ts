import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NavController } from '@ionic/angular';
import { ActivatedRoute } from '@angular/router';
import { CallNumber } from '@ionic-native/call-number/ngx';
@Component({
  selector: 'app-professors',
  templateUrl: './professors.page.html',
  styleUrls: ['./professors.page.scss'],
})
export class ProfessorsPage implements OnInit {
  // professors=Observable<any>;
  public baseURL;
  public url;
  dept: string;
  response: Object;
  constructor(private activatedRoute:ActivatedRoute, public navCtrl: NavController, public httpClient: HttpClient,private callNumber: CallNumber) {
    this.baseURL='http://localhost:8000/scrapdata/dept/';
  }
  public async Call(){
    
    this.callNumber.callNumber("18001010101", true)
    .then(res => console.log('Launched dialer!', res))
    .catch(err => console.log('Error launching dialer', err));
  };
  
  get(){
    let data={
        "dept":this.dept
    }
    const httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'}),
      }
    this.httpClient.post(this.baseURL,JSON.stringify(data),httpOptions).subscribe((res1)=>{
      console.log(res1); 
      this.response=res1;
    },(error:any)=>{console.log(error); });
    
  }
  ngOnInit() {
    this.dept=this.activatedRoute.snapshot.paramMap.get('deptname');
    console.log(this.dept)
    this.get()
  }
}
