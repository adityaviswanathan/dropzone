package com.dropzone.dropzone;

import android.app.Activity;
import android.location.Location;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ListView;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.model.LatLng;

import org.apache.http.client.methods.HttpGet;

import java.net.URI;
import java.util.ArrayList;

/**
 * Created by eddie_000 on 1/17/2015.
 */
public class MapsFragment extends Fragment {
    /**
     * The fragment argument representing the section number for this
     * fragment.
     */
    private static final String ARG_SECTION_NUMBER = "section_number";
    ListView dropList;
    GoogleMap.OnMyLocationChangeListener locationChangeListener;
    GoogleMap.OnMyLocationButtonClickListener locationButtonListener;
    public GoogleMap map;
    boolean centerMap;

    MainActivity mainActivity;
    NearbyDropRunnable nearbyDropRunnable;
    HttpGet nearbyDropsGet;

    public MapsFragment() {
        Bundle args = new Bundle();
        args.putInt(ARG_SECTION_NUMBER, 0);
        setArguments(args);
        centerMap = true;
        nearbyDropsGet = new HttpGet();

        nearbyDropRunnable = new NearbyDropRunnable(this, nearbyDropsGet);

        locationChangeListener = new GoogleMap.OnMyLocationChangeListener() {
            @Override
            public void onMyLocationChange(Location location) {
                if (centerMap) {
                    map.animateCamera(CameraUpdateFactory.newLatLng(makeLatLng(location)));
                }
                if (mainActivity.dbUserId == -1)
                    return;
                nearbyDropsGet.setURI(URI.create("http://dropzone.herokuapp.com/api/user/" +
                        mainActivity.dbUserId + "/nearby?lat=" + location.getLatitude() +
                        "&lng=" + location.getLongitude()));
                new Thread(nearbyDropRunnable).start();
            }
        };

        locationButtonListener = new GoogleMap.OnMyLocationButtonClickListener() {

            @Override
            public boolean onMyLocationButtonClick() {
                centerMap = true;
                return false;
            }
        };
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        mainActivity = (MainActivity) activity;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_map, container, false);
        dropList = (ListView) rootView.findViewById(R.id.drop_list);
        dropList.setAdapter(new DropAdapter(mainActivity));
        dropList.setDivider(null);
        return rootView;
    }

    @Override
    public void onViewStateRestored(Bundle savedInstanceState) {
        super.onViewStateRestored(savedInstanceState);

        // Obtain reference to google map instance
        SupportMapFragment mapFrag = (SupportMapFragment) getChildFragmentManager().findFragmentById(R.id.map);
        mapFrag.getMapAsync(new OnMapReadyCallback() {
            @Override
            public void onMapReady(GoogleMap googleMap) {
                map = googleMap;
                map.setMyLocationEnabled(true);
                map.setOnMyLocationChangeListener(locationChangeListener);
                map.setOnMyLocationButtonClickListener(locationButtonListener);
                // Set default zoom level
                map.moveCamera(CameraUpdateFactory.zoomTo(16));
            }
        });
    }

    public static LatLng makeLatLng(Location location) {
        return new LatLng(location.getLatitude(), location.getLongitude());
    }

}
