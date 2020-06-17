import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NavController } from '@ionic/angular';
import { ActivatedRoute } from '@angular/router';
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
  constructor(private activatedRoute:ActivatedRoute, public navCtrl: NavController, public httpClient: HttpClient) {
    this.baseURL='http://localhost:8000/scrapdata/dept/';
  }

  

  
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
