//
//  FirstViewController.swift
//  dropzone
//
//  Created by aditya on 1/17/15.
//  Copyright (c) 2015 Aditya Viswanathan. All rights reserved.
//

import UIKit
import MapKit

class FirstViewController: UIViewController {

    @IBOutlet weak var map: MKMapView!
    var loc = CLLocationCoordinate2D(
        latitude: 16.40,
        longitude: -86.34
    )
    var span = MKCoordinateSpanMake(1, 1)
//    var region = MKCoordinateRegion(center: loc, span: span)
//    map.setRegion(region, animated: true)
    override func viewDidLoad() {
        super.viewDidLoad()
        println("first view")
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

