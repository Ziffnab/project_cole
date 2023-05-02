using System;
using Newtonsoft.Json.Linq;

public partial class InterfaceManager : Component
{
    public string apiUrl { get; set; } = "";
    public bool enableDebugMode { get; set; } = false;

    private readonly HttpClient _httpClient;
    private const int maxHttpTimeoutSeconds = 30;

    [Inject]
    public InteractionRepository InteractionsDb => null;

    protected override void OnInit()
    {
        base.OnInit();

        _httpClient = new HttpClient(new JsonMediaTypeFormatter())
        {
            BaseAddressChanged += (sender, e) => InvalidateDisposable(),
            Timeout = TimeSpan.FromSeconds(maxHttpTimeoutSeconds),
            MaxConnectionsPerServer = 256
        };

        string html = TemplateLoader.LoadTemplate();
        if (!string.IsNullOrEmpty(html))
        {
            StartCoroutine(WaitAndUpdateInterface(html));
        }
        else
        {
            Debug.LogError("Failed to load interface template.");
        }
    }

    [OneShot]
    public async Task<APIResponse> SendRequestAsync<T>(string requestPath, object content = null, Dictionary<string, object> headers = null) where T : class, new()
    {
        var responseString = await _httpClient.PostAsTextAsync($"{apiUrl}{requestPath}", content, headers);
        return DeserializeApiResponse(responseString).Data as T ?? throw new NotSupportedException("Invalid response");
    }

    private static T DeserializeApiResponse<T>(string json)
    {
        try
        {
            return JObject.Parse(json)["data"].Value<T>();
        }
        catch
        {
            if (_logger != null)
                _logger.Error($"Failed deserializing JSON result: \"{json}\"");

            return default(T);
        }
    }

    private Disposable AddAuthTokenHeader(Dictionary<string, object> headers)
    {
        return headers["Authorization"] = $"Bearer *TODO*";
    }
}

[TableName("open_assistant_interactions")]
public class OpenAssistantInteraction : TableObject
{
    [PrimaryKey]
    [ColumnName("id")]
    public string Id {
        gusing System;
using Newtonsoft.Json.Linq;

public partial class InterfaceManager : Component
{
    public string apiUrl { get; set; } = "";
    public bool enableDebugMode { get; set; } = false;

    private readonly HttpClient _httpClient;
    private const int maxHttpTimeoutSeconds = 30;

    [Inject]
    public InteractionRepository InteractionsDb => null;

    protected override void OnInit()
    {
        base.OnInit();

        _httpClient = new HttpClient(new JsonMediaTypeFormatter())
        {
            BaseAddressChanged += (sender, e) => InvalidateDisposable(),
            Timeout = TimeSpan.FromSeconds(maxHttpTimeoutSeconds),
            MaxConnectionsPerServer = 256
        };
    }

    [OneShot]
    public async Task<APIResponse> SendRequestAsync<T>(string requestPath, object content = null, Dictionary<string, object> headers = null) where T : class, new()
    {
        var responseString = await _httpClient.PostAsTextAsync($"{apiUrl}{requestPath}", content, headers);
        return DeserializeApiResponse(responseString).Data as T ?? throw new NotSupportedException("Invalid response");
    }

    private static T DeserializeApiResponse<T>(string json)
    {
        try
        {
            return JObject.Parse(json)["data"].Value<T>();
        }
        catch
        {
            if (_logger != null)
                _logger.Error($"Failed deserializing JSON result: \"{json}\"");

            return default(T);
        }
    }

    private Disposable AddAuthTokenHeader(Dictionary<string, object> headers)
    {
        return headers["Authorization"] = $"Bearer *TODO*";
    }
}

[TableName("open_assistant_interactions")]
public class OpenAssistantInteraction : TableObject
{
    [PrimaryKey]
    [ColumnName("id")]
    public string Id { get; set; } = Guid.NewGuid().ToString(); // Use a random Guid to generate IDs

    [NotNullable]
    public DateTimeOffset Timestamp { get; init; } = DateTimeOffset.UtcNow;

    [JsonConverter(typeof(StringEnumDescriptionJsonConverter))]
    public OpenAssistantApiRequestResult? Result { get; set; }
}