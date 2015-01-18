package com.dropzone.dropzone;

import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.location.LocationManager;
import android.os.Looper;
import android.support.v7.app.ActionBarActivity;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.os.Bundle;
import android.support.v4.view.ViewPager;
import android.text.Html;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;

import com.facebook.Request;
import com.facebook.Response;
import com.facebook.Session;
import com.facebook.SessionState;
import com.facebook.model.GraphUser;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.StatusLine;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicHeader;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.protocol.HTTP;
import org.apache.http.util.EntityUtils;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends ActionBarActivity {

    /**
     * The {@link android.support.v4.view.PagerAdapter} that will provide
     * fragments for each of the sections. We use a
     * {@link FragmentPagerAdapter} derivative, which will keep every
     * loaded fragment in memory. If this becomes too memory intensive, it
     * may be best to switch to a
     * {@link android.support.v4.app.FragmentStatePagerAdapter}.
     */
    SectionsPagerAdapter mSectionsPagerAdapter;

    /**
     * The {@link ViewPager} that will host the section contents.
     */
    ViewPager mViewPager;

    public LocationManager locationManager;

    public GraphUser user;
    public HttpClient httpClient;
    public int dbUserId = -1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        android.support.v7.app.ActionBar bar = getSupportActionBar();
        bar.setBackgroundDrawable(new ColorDrawable(Color.parseColor("#2c7896")));
        getSupportActionBar().setTitle((Html.fromHtml("<font color=\"#ffffff\">" + getString(R.string.app_name) + "</font>")));
        httpClient = new DefaultHttpClient();

        locationManager = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);

        // Create the adapter that will return a fragment for each of the three
        // primary sections of the activity.
        mSectionsPagerAdapter = new SectionsPagerAdapter(getSupportFragmentManager());

        // Set up the ViewPager with the sections adapter.
        mViewPager = (ViewPager) findViewById(R.id.pager);
        mViewPager.setAdapter(mSectionsPagerAdapter);
        openFacebookSession();
    }

    @Override
    protected void onResume() {
        super.onResume();
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }


    /**
     * A {@link FragmentPagerAdapter} that returns a fragment corresponding to
     * one of the sections/tabs/pages.
     */
    public class SectionsPagerAdapter extends FragmentPagerAdapter {

        public SectionsPagerAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int position) {
            // getItem is called to instantiate the fragment for the given page.
            switch (position) {
                case 0:
                    return new MapsFragment();
                case 1:
                    return new DropFragment();
                default:
                    return null; // TODO: throw something?
            }
        }

        @Override
        public int getCount() {
            // Show 2 total pages.
            return 2;
        }

        @Override
        public CharSequence getPageTitle(int position) {
            Locale l = Locale.getDefault();
            switch (position) {
                case 0:
                    return getString(R.string.title_section1).toUpperCase(l);
                case 1:
                    return getString(R.string.title_section2).toUpperCase(l);
//                case 2:
//                    return getString(R.string.title_section3).toUpperCase(l);
            }
            return null;
        }
    }

    private void openFacebookSession() {
        openActiveSession(this, true, Arrays.asList(new String[]{"email"}), new Session.StatusCallback() {

            @Override
            public void call(final Session session, SessionState sessionState, Exception e) {
                if (e != null) {
                    Log.e("Facebook", e.getMessage());
                }
                else if (sessionState == SessionState.OPENED) {
                    Log.d("Facebook", "Session State: " + session.getState());
                    Request request = Request.newMeRequest(session, new Request.GraphUserCallback() {
                        @Override
                        public void onCompleted(GraphUser graphUser, Response response) {
                            // If the response is successful
                            if (session == Session.getActiveSession()) {
                                if (graphUser != null) {
                                    user = graphUser;
                                    JSONObject json = user.getInnerJSONObject();
                                    try {
                                        json.put("photo", "https://graph.facebook.com/" + user.getId() + "/picture");
                                    } catch (JSONException e1) {
                                        e1.printStackTrace();
                                    }
                                    Log.i("JSON user data", json.toString());
                                    sendJson(httpClient, "http://dropzone.herokuapp.com/api/user", json, new POSTCallback() {
                                        @Override
                                        public void onResponse(HttpResponse response) {
                                            try {
                                                // TODO: kill me
                                                JSONObject responsePayload = new JSONObject(EntityUtils.toString(response.getEntity()));
                                                Log.i("Nearby Drops Response Payload", responsePayload.toString());
                                                dbUserId = responsePayload.getJSONObject("user").getInt("id");;
                                            } catch (IOException | JSONException e1) {
                                                e1.printStackTrace();
                                            }

                                            Log.i("USER ID", "" + dbUserId);
                                        }
                                    });
                                }
                            }
                        }
                    });
                    Bundle params = request.getParameters();
                    params.putString("fields", "email,name");
                    request.setParameters(params);
                    request.executeAsync();
                    Log.i("USER POST", "Execution queued");
//                    Request.executeBatchAsync(request);
                }
            }
        });
    }

    public static void sendJson(final HttpClient client, final String url, final JSONObject json, final POSTCallback callback) {
        Thread t = new Thread() {

            public void run() {
                Looper.prepare(); //For Preparing Message Pool for the child Thread
                HttpConnectionParams.setConnectionTimeout(client.getParams(), 10000); //Timeout Limit
                HttpResponse response;

                try {
                    HttpPost post = new HttpPost(url);
                    StringEntity se = new StringEntity(json.toString());
                    se.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
                    post.setEntity(se);
                    response = client.execute(post);
                    /* Process response */
                    if (response != null) {
                        StatusLine status = response.getStatusLine();
                        if (status.getStatusCode() != 200) {
                            String payload = EntityUtils.toString(response.getEntity());
                            Log.e("HTTP USER RESPONSE ERROR", status.toString());
                            Log.e("HTTP USER RESPONSE PAYLOAD", payload);
                            return;
                        }
                        if (callback != null) {
                            Log.i("HTTP USER RESPONSE", status.toString());
                            callback.onResponse(response); //Get the data in the entity
                        }
                    }

                } catch (Exception e) {
                    e.printStackTrace();
                }

                Looper.loop(); //Loop in the message queue
            }
        };

        t.start();
    }

    private static Session openActiveSession(Activity activity, boolean allowLoginUI, List permissions, Session.StatusCallback callback) {
        Session.OpenRequest openRequest = new Session.OpenRequest(activity).setPermissions(permissions).setCallback(callback);
        Session session = new Session.Builder(activity).build();
        if (SessionState.CREATED_TOKEN_LOADED.equals(session.getState()) || allowLoginUI) {
            Session.setActiveSession(session);
            session.openForRead(openRequest);
            return session;
        }
        return null;
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        Session.getActiveSession().onActivityResult(this, requestCode, resultCode, data);
    }
}
